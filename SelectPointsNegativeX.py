import c4d
from c4d import gui

def main():
    doc.StartUndo()
    selectedObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    for obj in selectedObjects:
        if not isinstance(obj, c4d.PolygonObject):
            continue
        points = obj.GetAllPoints()
        sel = obj.GetPointS()
        doc.AddUndo(c4d.UNDOTYPE_CHANGE_SELECTION, obj)
        for i in range(0, obj.GetPointCount()):
            point = obj.GetPoint(i)
            if point.x < 0:
                sel.Select(i)
    doc.EndUndo()
    c4d.EventAdd()
    c4d.CallCommand(12139) # Points

if __name__=='__main__':
    main()
