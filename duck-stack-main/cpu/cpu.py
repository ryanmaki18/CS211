"""
Duck Machine model DM2022 CPU
"""

import context  #  Python import search from project root
from instruction_set.instr_format import Instruction, OpCode, CondFlag, decode
# The CPU will need to use a Memory and Registers,
# as well as model-view-controller components for displaying the CPU state.

from cpu.memory import Memory
from cpu.register import Register, ZeroRegister
from cpu.mvc import MVCEvent, MVCListenable

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class ALU(object):
    """The arithmetic logic unit (also called a "functional unit"
    in a modern CPU) executes a selected function but does not
    otherwise manage CPU state. A modern CPU core may have several
    ALUs to boost performance by performing multiple operatons
    in parallel, but the Duck Machine has just one ALU in one core.
    """
    # The ALU chooses one operation to apply based on a provided
    # operation code.  These are just simple functions of two arguments;
    # in hardware we would use a multiplexer circuit to connect the
    # inputs and output to the selected circuitry for each operation.
    ALU_OPS = {
        OpCode.ADD: lambda x, y: x + y,
        OpCode.SUB: lambda x, y: x - y,
        OpCode.MUL: lambda x, y: x * y,
        OpCode.DIV: lambda x, y: x // y,
        # For memory access operations load, store, the ALU
        # performs the address calculation
        OpCode.LOAD: lambda x, y: x + y,
        OpCode.STORE: lambda x, y: x + y,
        # Some operations perform no operation
        OpCode.HALT: lambda x, y: 0
    }

    def exec(self, op: OpCode, in1: int, in2: int) -> tuple[int, CondFlag]:
        try:
            result = self.ALU_OPS[op](in1, in2)  # refers to ALU_OPS dict above
            if (0 + result) == 0:
                return result, CondFlag.Z
            elif (0 + result) > 0:
                return result, CondFlag.P
            elif (0 + result) < 0:
                return result, CondFlag.M
        except Exception as e:
            return 0, CondFlag.V

class CPUStep(MVCEvent):
    """CPU is beginning step with PC at a given address"""
    def __init__(self, subject: "CPU", pc_addr: int,
                 instr_word: int, instr: Instruction)-> None:
        self.subject = subject
        self.pc_addr = pc_addr
        self.instr_word = instr_word
        self.instr = instr


class CPU(MVCListenable):
    """Duck Machine central processing unit (CPU)
    has 16 registers (including r0 that always holds zero
    and r15 that holds the program counter), a few
    flag registers (condition codes, halted state),
    and some logic for sequencing execution.  The CPU
    does not contain the main memory but has a bus connecting
    it to a separate memory.
    """

    def __init__(self, memory: Memory):
        super().__init__()
        self.memory = memory  # Not part of CPU; what we really have is a connection
        self.registers = [ZeroRegister(), Register(), Register(), Register(),
                          Register(), Register(), Register(), Register(),
                          Register(), Register(), Register(), Register(),
                          Register(), Register(), Register(), Register()]
        self.condition = CondFlag.ALWAYS
        self.halted = False
        self.alu = ALU()
        self.pc = self.registers[15]

    def step(self):
        """One fetch/decode/execute step"""
        ## Fetch
        instr_addr = self.pc.get()
        instr_word = self.memory.get(instr_addr)

        ## Decode
        instr = decode(instr_word)
        # Display the CPU state when we have decoded the instruction,
        # before we have executed it
        self.notify_all(CPUStep(self, instr_addr, instr_word, instr))

        ## Execute
        predicate = self.condition.value & instr.cond.value
        if predicate > 0:
            left = self.registers[instr.reg_src1].get()  # Left Operand
            right = instr.offset + self.registers[instr.reg_src2].get()  # Right Operand
            result_value, result_cond = self.alu.exec(instr.op, left, right)  # returns result value and condition code

            # Incrementing program counter
            value = self.pc.get()
            value += 1
            self.pc.put(value)

            # After incrementing the program counter, we complete the operation.
            if instr.op == OpCode.STORE:
                self.memory.put(result_value, self.registers[instr.reg_target].get())
            elif instr.op == OpCode.LOAD:
                self.registers[instr.reg_target].put(self.memory.get(result_value))
            elif instr.op == OpCode.HALT:
                self.halted = True
            else:
                self.registers[instr.reg_target].put(result_value)
                self.condition = result_cond
        else:
            value = self.pc.get()  # if predicate not satisfied, we skip most steps and increment register 15
            value += 1
            self.pc.put(value)


    def run(self, from_addr=0, single_step=False) -> None:
        """Step the CPU until it executes a HALT. (Executes fetch/decode/execute cycle of step over and over again)"""
        self.halted = False
        self.registers[15].put(from_addr)
        step_count = 0
        while not self.halted:
            if single_step:
                input(f"Step {step_count}; press enter")
            self.step()
            step_count += 1
