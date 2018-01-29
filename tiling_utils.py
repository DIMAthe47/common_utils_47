from math import ceil


def generate_tiles_rects(rect_shape, tile_shape, tile_step, generator_mode=False):
    generator_ = gen_slice_rect(rect_shape, tile_shape, tile_step)
    if generator_mode:
        return generator_
    else:
        tiles_rects = list(generator_)
        return tiles_rects


def gen_slice_rect(rect_size, tile_size, tile_step):
    # tiles_rects = []
    x, y = (0, 0)
    rect_width, rect_height = rect_size
    tile_width, tile_height = tile_size
    x_step, y_step = tile_step
    while y < rect_height:
        while x < rect_width:
            w = min((tile_width, rect_width - x))
            h = min((tile_height, rect_height - y))
            rect = (x, y, w, h)
            yield rect
            # tiles_rects.append((x, y, w, h))
            x += x_step
        x = 0
        y += y_step

        # print("rect_size", rect_size)
        # print("rects_sliced", tiles_rects)


def gen_slice_rect_n(rect_size, columns, rows):
    # tiles_rects = []
    x, y = (0, 0)
    rect_width, rect_height = rect_size
    tile_width, tile_height = rect_width / columns, rect_height / rows
    x_step, y_step = tile_width, tile_height
    while y < rect_height:
        while x < rect_width:
            w = min((tile_width, rect_width - x))
            h = min((tile_height, rect_height - y))
            rect = (x, y, w, h)
            yield rect
            # tiles_rects.append((x, y, w, h))
            x += x_step
        x = 0
        y += y_step


def get_n_columns_n_rows_for_tile_size(rect_size, tile_size):
    n_columns = rect_size[0] / tile_size[0]
    n_rows = rect_size[1] / tile_size[1]
    if tile_size[0] * n_columns < rect_size[0]:
        n_columns += 1
    if tile_size[1] * n_rows < rect_size[1]:
        n_rows += 1
    return n_columns, n_rows



def slice_rect2(rect_size, tile_size, tile_step):
    x_size, y_size = rect_size
    x_step, y_step = tile_step

    cols = ceil(x_size / x_step)
    rows = ceil(y_size / y_step)
    rects = [
        (
            (j - 1) * x_step + tile_size[0],
            (i - 1) * y_step + tile_size[1],
            tile_size[0],
            tile_size[1]
        )
        for i in range(rows) for j in range(cols)
    ]

    if cols != x_size // x_step:
        for i in range(rows):
            rect = list(rects[i * cols + cols - 1])
            rect[2] = x_size - rect[0]
            rects[i * cols + cols - 1] = tuple(rect)
    if rows != y_size // y_step:
        for j in range(cols):
            rect = list(rects[(rows - 1) * cols + j])
            rect[3] = y_size - rect[1]
            rects[(rows - 1) * cols + j] = tuple(rect)

    return rects

