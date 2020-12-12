def bres2(x0, y0, x1, y1, plot, block, length):
  dx = x1 - x0
  dy = y1 - y0

  xsign = 1 if dx > 0 else -1
  ysign = 1 if dy > 0 else -1

  dx = abs(dx)
  dy = abs(dy)

  if dx > dy:
    xx, xy, yx, yy = xsign, 0, 0, ysign
  else:
    dx, dy = dy, dx
    xx, xy, yx, yy = 0, ysign, xsign, 0

  D = 2*dy - dx
  y = 0

  for x in range(dx + 1):
    if x > length:
      return
    XPOS = x0 + x*xx + y*yx
    YPOS = y0 + x*xy + y*yy
    plot(XPOS, YPOS)
    if block(XPOS, YPOS):
      return
    if D >= 0:
      y += 1
      D -= 2*dx
    D += 2*dy

