"""

Cell: One rectangle where one single form is placed
Cell gridlines: The fine grid inside each Cell
Main Grid: The big grid on the canvas, where each Cell sits 

Updated January 02 2021
"""


def get_cell_gridlines(cell_x, cell_y, cw, ch, margin, _sq=8):
    """Returns two lists gx and gy with fine grid coordinates"""

    gx, gy = [], []

    for s in range(_sq + 1):
        gx.append(cell_x + margin + (cw / _sq * s))
        gy.append(cell_y + margin + (ch / _sq * s))
    return gx, gy


def draw_cell_gridlines(cell_x, cell_y, gx, gy, sq=8):
    """

        sq is the number of squares in one Grid Box
    """

    for s in range(sq + 1):
        line(gx[s], gy[0], gx[s], gy[sq])  # verts
        line(gx[0], gy[s], gx[sq], gy[s])  # horiz


class Grid:

    """Represents a large rectangular grid on the screen.
    
    And there is a rectangle (a bounding box) for the grid
    Inside it are 'cells' in rows and columns
    
    Canvas: The drawing area for this grid.
    Cell: Interior rectangles inside the current grid

    """

    def __init__(
        self,
        num_rows,
        num_cols,
        canvas_width,
        canvas_height,
        canvas_x_margin=0,
        canvas_y_margin=0,
        grid_nw_x=0,  # useful if you have multiple Grids, esp for tiling
        grid_nw_y=0,
    ):

        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cells = []  # list of cells in the Grid
        self.nw_corners = []
        self.cell_width = (canvas_width - (2 * canvas_x_margin)) / num_cols
        self.cell_height = (canvas_height - (2 * canvas_y_margin)) / num_rows
        self.grid_xmargin = canvas_x_margin
        self.grid_ymargin = canvas_y_margin
        self.grid_nw_x = grid_nw_x
        self.grid_nw_y = grid_nw_y

        cw = self.cell_width
        ch = self.cell_height

        # Create cell objects
        xstart, ystart = self.grid_nw_x, self.grid_nw_y
        xmargin, ymargin = self.grid_xmargin, self.grid_ymargin
        ##        print(xstart, ystart)
        #       print("num rows", num_rows)
        cell_id = 0
        for row in range(num_rows):
            for col in range(num_cols):
                cx, cy = (
                    xstart + xmargin + col * cw,
                    ystart + ymargin + ch * row,
                )  # NW corner of each cell
                # print(cx, cy, "RC", row, col, ch, cw)
                cell = Cell(cx, cy, cw, ch, cell_id)  # create Cell object
                # address of this particular cell within grid
                cell.row, cell.col = (row, col)
                cell.gx, cell.gy = get_cell_gridlines(cx, cy, cw, ch, margin=0)
                cell.cx, cell.cy = cx + cw / 2, cy - ch / 2  # cell centers
                self.cells.append(cell)
                self.nw_corners.append((cx, cy))
                cell_id += 1

    def render_grid_border(self, fill_color=None):
        """One large rectangle for the entire grid border, with all the cells inside"""

        pushStyle()
        strokeWeight(3)
        stroke(0)
        if fill_color:
            print(fill_color)
            fill(*fill_color)
        else:
            noFill()
        rect(
            self.grid_nw_x,
            self.grid_nw_y,
            self.num_cols * self.cell_width,
            self.cell_height * self.num_rows,
        )
        popStyle()

    def render_cell_borders(self):
        """Draws the borders for each cell in the grid"""

        rectMode(CORNER)
        # print(
        #     self.grid_xmargin, self.grid_ymargin, self.cell_height, self.cell_width
        # )
        for row in range(self.num_rows):
            lstart_y = self.grid_ymargin + row * self.cell_height
            for col in range(self.num_cols):
                lstart_x = self.grid_xmargin + col * self.cell_width
                rect(lstart_x, lstart_y, self.cell_width, self.cell_height)

    def render_cells(self, show_gridlines=False):
        # This will only work in Cell Objects have been created first
        for l in self.cells:
            l.render()
            if show_gridlines:
                l.render_gridlines()

    def get_cell(self, _rownum, _colnum, verbose=False):
        cellnum = self.num_cols * _rownum + _colnum
        if verbose:
            print(cellnum, _rownum, _colnum)
        return self.cells[cellnum]


class Cell(object):
    def __init__(self, _x, _y, _width, _height, _id):
        self.x, self.y = _x, _y
        self.id = _id
        self.width = _width
        self.height = _height

    def fill_cell(self, _color=0):
        fill(*_color)
        rect(self.x, self.y, self.width, self.height)

    def render(self):
        # x,y is the top left corner (NW corner)
        #        shp_opt = generate_base()
        xoffset = self.x + self.width / 2
        yoffset = self.y + self.height * 3 / 4
        # render_element("base", shp_opt, xoffset, yoffset, self.width, self.height)
        noFill()
        strokeWeight(2)

    #        st, end, _dir = render_outline(self.x, self.y, self.gx, self.gy)
    #        render_cell_interior(st, end, _dir, self.gx, self.gy)
    #        render_cell_top(st, end, _dir, self.gx, self.gy)
    #        render_cell_base(st, end, _dir, self.gx, self.gy)
    # change this to become form.render() and cell.render only draws bg maybe

    def render_gridlines(self):
        """ Draws Lines interior to a cell"""
        gx, gy = get_cell_gridlines(
            self.x, self.y, self.width, self.height, margin=0, _sq=8
        )
        draw_cell_gridlines(self.x, self.y, gx, gy)

