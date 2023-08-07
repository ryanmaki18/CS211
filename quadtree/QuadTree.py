# Encoding an Image as a QuadTree
# CS 211 -- Optional Assignment
# March 16, 2023


# Symbols in the input string
BLACK = "B"
WHITE = "W"
GREY = "G"

# Symbols in the grid and string representation of the image
BLACK_PIXEL = "X"
WHITE_PIXEL = "."


def fresh_grid() -> list[list[str]]:
    """A fresh 8x8 grid, filled initially with an invalid character"""
    grid = []
    for row in range(8):
        grid.append(["@"] * 8)
    return grid


def fill_region(grid: list[list[str]],
                row_l: int, col_l: int,
                size: int, fill_with: str):
    """Fill grid[row_l:row_l+size][col_l:col_l+size] with fill_with"""
    for row in range(row_l, row_l+size):
        for col in range(col_l, col_l+size):
            grid[row][col] = fill_with


def decode(s: str) -> str:
    """s is a prefix encoding of a quadtree representation
    of an 8x8 grid.  'B' represents a black quadrant (all 'X'), 'W'
    represents a white quadrant (all '-'), and 'G' represents a grey
    quadrant (mix of black and white).
    The returned grid is a list of 8 strings, each with 8
    characters, all either '-' or 'X'
    """
    grid = fresh_grid()
    s_pos = 0

    def r_decode(row: int, col: int, size: int):
        """Process the next element of s"""
        nonlocal s_pos
        nonlocal grid

        command = s[s_pos]
        s_pos += 1
        # --------------------------------------
        if command == BLACK:
            fill_region(grid, row, col, size, BLACK_PIXEL)
        elif command == WHITE:
            fill_region(grid, row, col, size, WHITE_PIXEL)
        elif command == GREY:
            new_size = size // 2
            r_decode(row, col, new_size)  # NW
            r_decode(row, col + new_size, new_size)  # NE
            r_decode(row + new_size, col + new_size, new_size)  # SE
            r_decode(row + new_size, col, new_size)  # SW
        # --------------------------------------

    r_decode(0, 0, 8)  # Start with the whole 8x8 grid
    return "\n".join(["".join(row) for row in grid])


class QuadTree:
    """A quadtree representation of a monochrome image.
    Restriction:  Imagine is square with side a power of 2,
    to avoid dealing with "off-screen" portions of image.
    """
    pass


class Leaf(QuadTree):
    """A leaf represents a solid block. This class includes only singletons,
    which we use as constants!
    """
    def __init__(self, symbol: str):
        """symbol is the character we use in the linearized representation"""
        self.symbol = symbol

    def __str__(self) -> str:
        # The linear representation of the quadtree
        return self.symbol


BLACK_NODE = Leaf(BLACK)  # Just one black node, so we can compare with "is"
WHITE_NODE = Leaf(WHITE)  # Just one white node, so we can compare with "is"


class GreyNode(QuadTree):
    def __init__(self, nw: QuadTree, ne: QuadTree, se: QuadTree, sw: QuadTree):
        self.nw = nw  # Northwest quadrant
        self.ne = ne  # Northeast quadrant
        self.se = se  # Southeast quadrant
        self.sw = sw  # Southwest quadrant

    def __str__(self) -> str:
        # Linear representation of the QuadTree
        return "G" + str(self.nw) + str(self.ne) + str(self.se) + str(self.sw)


def str_to_grid(s: str) -> list[list[str]]:
    """Convert 8 lines of 8 characters, separated by newline
    into 8x8 matrix of characters.
    """
    lines = s.strip().splitlines() # Ignore beginning or ending newline, for convenience
    assert len(lines) == 8, "Wrong number of lines, should be 8"
    for line in lines:
        assert len(line) == 8, "Line length wrong, should be 8"
    grid = [[ch for ch in line] for line in lines]
    return grid


def build_quad_tree(grid: list[list[str]], row_l: int, col_l: int, size: int) -> QuadTree:
    """Return quadtree representation of grid[row_l:row_l+size][col_l:col_l+size]"""
    if size == 1:
        if grid[row_l][col_l] is BLACK_PIXEL:
            return BLACK
        if grid[row_l][col_l] is WHITE_PIXEL:
            return WHITE
    new_size = size // 2
    nw = build_quad_tree(grid, row_l, col_l, new_size)
    ne = build_quad_tree(grid, row_l, col_l + new_size, new_size)  # NE
    se = build_quad_tree(grid, row_l + new_size, col_l + new_size, new_size)  # SE
    sw = build_quad_tree(grid, row_l + new_size, col_l, new_size)  # SW
    if nw is BLACK and ne is BLACK and se is BLACK and sw is BLACK:
        return BLACK
    elif nw is WHITE and ne is WHITE and se is WHITE and sw is WHITE:
        return WHITE
    else:
        return GreyNode(nw, ne, se, sw)
    
