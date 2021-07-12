from geometry.rectangle import Rectangle as GRectangle
from view.components.drawObject import DrawObject


class Rectangle(DrawObject, GRectangle):
    def __init__(self, canvas, center, sides):
        DrawObject.__init__(self,canvas)
        GRectangle.__init__(self, center, sides)
        self.set_position((center.get_x(), center.get_y()))

    def draw(self):
        vert_map = []
        c = self.centroid.get_draw_position()
        for v in self.vertices:
            vert_map.extend([v.get_x(c), v.get_y(c)])
        self.canvas.create_polygon(vert_map, fill=self.color["fill"].hex)
        return self