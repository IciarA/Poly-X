# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_Tesy')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_Tesy')
    _Tesy = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Tesy', [dirname(__file__)])
        except ImportError:
            import _Tesy
            return _Tesy
        try:
            _mod = imp.load_module('_Tesy', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _Tesy = swig_import_helper()
    del swig_import_helper
else:
    import _Tesy
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Tesy.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _Tesy.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _Tesy.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _Tesy.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _Tesy.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _Tesy.SwigPyIterator_equal(self, x)

    def copy(self):
        return _Tesy.SwigPyIterator_copy(self)

    def next(self):
        return _Tesy.SwigPyIterator_next(self)

    def __next__(self):
        return _Tesy.SwigPyIterator___next__(self)

    def previous(self):
        return _Tesy.SwigPyIterator_previous(self)

    def advance(self, n):
        return _Tesy.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _Tesy.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _Tesy.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _Tesy.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _Tesy.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _Tesy.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _Tesy.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _Tesy.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class VecFloat(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecFloat, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecFloat, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _Tesy.VecFloat_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _Tesy.VecFloat___nonzero__(self)

    def __bool__(self):
        return _Tesy.VecFloat___bool__(self)

    def __len__(self):
        return _Tesy.VecFloat___len__(self)

    def __getslice__(self, i, j):
        return _Tesy.VecFloat___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _Tesy.VecFloat___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _Tesy.VecFloat___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _Tesy.VecFloat___delitem__(self, *args)

    def __getitem__(self, *args):
        return _Tesy.VecFloat___getitem__(self, *args)

    def __setitem__(self, *args):
        return _Tesy.VecFloat___setitem__(self, *args)

    def pop(self):
        return _Tesy.VecFloat_pop(self)

    def append(self, x):
        return _Tesy.VecFloat_append(self, x)

    def empty(self):
        return _Tesy.VecFloat_empty(self)

    def size(self):
        return _Tesy.VecFloat_size(self)

    def swap(self, v):
        return _Tesy.VecFloat_swap(self, v)

    def begin(self):
        return _Tesy.VecFloat_begin(self)

    def end(self):
        return _Tesy.VecFloat_end(self)

    def rbegin(self):
        return _Tesy.VecFloat_rbegin(self)

    def rend(self):
        return _Tesy.VecFloat_rend(self)

    def clear(self):
        return _Tesy.VecFloat_clear(self)

    def get_allocator(self):
        return _Tesy.VecFloat_get_allocator(self)

    def pop_back(self):
        return _Tesy.VecFloat_pop_back(self)

    def erase(self, *args):
        return _Tesy.VecFloat_erase(self, *args)

    def __init__(self, *args):
        this = _Tesy.new_VecFloat(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _Tesy.VecFloat_push_back(self, x)

    def front(self):
        return _Tesy.VecFloat_front(self)

    def back(self):
        return _Tesy.VecFloat_back(self)

    def assign(self, n, x):
        return _Tesy.VecFloat_assign(self, n, x)

    def resize(self, *args):
        return _Tesy.VecFloat_resize(self, *args)

    def insert(self, *args):
        return _Tesy.VecFloat_insert(self, *args)

    def reserve(self, n):
        return _Tesy.VecFloat_reserve(self, n)

    def capacity(self):
        return _Tesy.VecFloat_capacity(self)
    __swig_destroy__ = _Tesy.delete_VecFloat
    __del__ = lambda self: None
VecFloat_swigregister = _Tesy.VecFloat_swigregister
VecFloat_swigregister(VecFloat)

class Segment(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Segment, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Segment, name)
    __repr__ = _swig_repr
    __swig_setmethods__["pointA"] = _Tesy.Segment_pointA_set
    __swig_getmethods__["pointA"] = _Tesy.Segment_pointA_get
    if _newclass:
        pointA = _swig_property(_Tesy.Segment_pointA_get, _Tesy.Segment_pointA_set)
    __swig_setmethods__["pointB"] = _Tesy.Segment_pointB_set
    __swig_getmethods__["pointB"] = _Tesy.Segment_pointB_get
    if _newclass:
        pointB = _swig_property(_Tesy.Segment_pointB_get, _Tesy.Segment_pointB_set)
    __swig_setmethods__["label"] = _Tesy.Segment_label_set
    __swig_getmethods__["label"] = _Tesy.Segment_label_get
    if _newclass:
        label = _swig_property(_Tesy.Segment_label_get, _Tesy.Segment_label_set)

    def __init__(self, *args):
        this = _Tesy.new_Segment(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def segmentDistance(self, p):
        return _Tesy.Segment_segmentDistance(self, p)

    def arcLength(self, p):
        return _Tesy.Segment_arcLength(self, p)
    __swig_destroy__ = _Tesy.delete_Segment
    __del__ = lambda self: None
Segment_swigregister = _Tesy.Segment_swigregister
Segment_swigregister(Segment)

VX = _Tesy.VX
VY = _Tesy.VY
VZ = _Tesy.VZ
VW = _Tesy.VW
PA = _Tesy.PA
PB = _Tesy.PB
PC = _Tesy.PC
PD = _Tesy.PD
RED = _Tesy.RED
GREEN = _Tesy.GREEN
BLUE = _Tesy.BLUE
KA = _Tesy.KA
KD = _Tesy.KD
KS = _Tesy.KS
ES = _Tesy.ES
EPSILON = _Tesy.EPSILON
class vec2(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec2, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _Tesy.new_vec2(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __iadd__(self, v):
        return _Tesy.vec2___iadd__(self, v)

    def __isub__(self, v):
        return _Tesy.vec2___isub__(self, v)

    def __imul__(self, d):
        return _Tesy.vec2___imul__(self, d)

    def __itruediv__(self, *args):
        return _Tesy.vec2___itruediv__(self, *args)
    __idiv__ = __itruediv__



    def Length(self):
        return _Tesy.vec2_Length(self)

    def SqrLength(self):
        return _Tesy.vec2_SqrLength(self)

    def Normalize(self):
        return _Tesy.vec2_Normalize(self)
    __swig_destroy__ = _Tesy.delete_vec2
    __del__ = lambda self: None
vec2_swigregister = _Tesy.vec2_swigregister
vec2_swigregister(vec2)
cvar = _Tesy.cvar
M_PI = cvar.M_PI
M_PI_2 = cvar.M_PI_2
M2_PI = cvar.M2_PI
Rad2Deg = cvar.Rad2Deg
Deg2Rad = cvar.Deg2Rad

class vec3(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec3, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec3, name)
    __repr__ = _swig_repr
    __swig_setmethods__["n"] = _Tesy.vec3_n_set
    __swig_getmethods__["n"] = _Tesy.vec3_n_get
    if _newclass:
        n = _swig_property(_Tesy.vec3_n_get, _Tesy.vec3_n_set)

    def __init__(self, *args):
        this = _Tesy.new_vec3(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __iadd__(self, v):
        return _Tesy.vec3___iadd__(self, v)

    def __isub__(self, v):
        return _Tesy.vec3___isub__(self, v)

    def __imul__(self, d):
        return _Tesy.vec3___imul__(self, d)

    def __itruediv__(self, *args):
        return _Tesy.vec3___itruediv__(self, *args)
    __idiv__ = __itruediv__



    def set(self, x, y, z):
        return _Tesy.vec3_set(self, x, y, z)

    def Length(self):
        return _Tesy.vec3_Length(self)

    def SqrLength(self):
        return _Tesy.vec3_SqrLength(self)

    def Normalize(self):
        return _Tesy.vec3_Normalize(self)

    def Cross(self, v):
        return _Tesy.vec3_Cross(self, v)

    def Print(self, title):
        return _Tesy.vec3_Print(self, title)
    __swig_destroy__ = _Tesy.delete_vec3
    __del__ = lambda self: None
vec3_swigregister = _Tesy.vec3_swigregister
vec3_swigregister(vec3)

def Prod(*args):
    return _Tesy.Prod(*args)
Prod = _Tesy.Prod

def Dot(*args):
    return _Tesy.Dot(*args)
Dot = _Tesy.Dot

def Distance(a, b):
    return _Tesy.Distance(a, b)
Distance = _Tesy.Distance

def DistanceSqr(a, b):
    return _Tesy.DistanceSqr(a, b)
DistanceSqr = _Tesy.DistanceSqr

class vec4(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec4, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec4, name)
    __repr__ = _swig_repr
    __swig_setmethods__["n"] = _Tesy.vec4_n_set
    __swig_getmethods__["n"] = _Tesy.vec4_n_get
    if _newclass:
        n = _swig_property(_Tesy.vec4_n_get, _Tesy.vec4_n_set)

    def __init__(self, *args):
        this = _Tesy.new_vec4(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def set(self, x, y, z, w):
        return _Tesy.vec4_set(self, x, y, z, w)

    def Print(self, title):
        return _Tesy.vec4_Print(self, title)
    __swig_destroy__ = _Tesy.delete_vec4
    __del__ = lambda self: None
vec4_swigregister = _Tesy.vec4_swigregister
vec4_swigregister(vec4)
axisX = cvar.axisX
axisY = cvar.axisY
axisZ = cvar.axisZ
vec3Zero = cvar.vec3Zero

class Corner(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Corner, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Corner, name)
    __repr__ = _swig_repr
    __swig_setmethods__["point"] = _Tesy.Corner_point_set
    __swig_getmethods__["point"] = _Tesy.Corner_point_get
    if _newclass:
        point = _swig_property(_Tesy.Corner_point_get, _Tesy.Corner_point_set)
    __swig_setmethods__["seg1"] = _Tesy.Corner_seg1_set
    __swig_getmethods__["seg1"] = _Tesy.Corner_seg1_get
    if _newclass:
        seg1 = _swig_property(_Tesy.Corner_seg1_get, _Tesy.Corner_seg1_set)
    __swig_setmethods__["seg2"] = _Tesy.Corner_seg2_set
    __swig_getmethods__["seg2"] = _Tesy.Corner_seg2_get
    if _newclass:
        seg2 = _swig_property(_Tesy.Corner_seg2_get, _Tesy.Corner_seg2_set)
    __swig_setmethods__["label"] = _Tesy.Corner_label_set
    __swig_getmethods__["label"] = _Tesy.Corner_label_get
    if _newclass:
        label = _swig_property(_Tesy.Corner_label_get, _Tesy.Corner_label_set)

    def __init__(self, *args):
        this = _Tesy.new_Corner(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def setSeg1(self, s):
        return _Tesy.Corner_setSeg1(self, s)

    def setSeg2(self, s):
        return _Tesy.Corner_setSeg2(self, s)

    def cornerDistance(self, p):
        return _Tesy.Corner_cornerDistance(self, p)

    def cornerRatio(self, p):
        return _Tesy.Corner_cornerRatio(self, p)
    __swig_destroy__ = _Tesy.delete_Corner
    __del__ = lambda self: None
Corner_swigregister = _Tesy.Corner_swigregister
Corner_swigregister(Corner)

class Polygon(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Polygon, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Polygon, name)
    __repr__ = _swig_repr
    __swig_setmethods__["low_bound"] = _Tesy.Polygon_low_bound_set
    __swig_getmethods__["low_bound"] = _Tesy.Polygon_low_bound_get
    if _newclass:
        low_bound = _swig_property(_Tesy.Polygon_low_bound_get, _Tesy.Polygon_low_bound_set)
    __swig_setmethods__["upper_bound"] = _Tesy.Polygon_upper_bound_set
    __swig_getmethods__["upper_bound"] = _Tesy.Polygon_upper_bound_get
    if _newclass:
        upper_bound = _swig_property(_Tesy.Polygon_upper_bound_get, _Tesy.Polygon_upper_bound_set)
    __swig_setmethods__["center"] = _Tesy.Polygon_center_set
    __swig_getmethods__["center"] = _Tesy.Polygon_center_get
    if _newclass:
        center = _swig_property(_Tesy.Polygon_center_get, _Tesy.Polygon_center_set)
    __swig_setmethods__["rotation"] = _Tesy.Polygon_rotation_set
    __swig_getmethods__["rotation"] = _Tesy.Polygon_rotation_get
    if _newclass:
        rotation = _swig_property(_Tesy.Polygon_rotation_get, _Tesy.Polygon_rotation_set)
    __swig_setmethods__["width"] = _Tesy.Polygon_width_set
    __swig_getmethods__["width"] = _Tesy.Polygon_width_get
    if _newclass:
        width = _swig_property(_Tesy.Polygon_width_get, _Tesy.Polygon_width_set)
    __swig_setmethods__["height"] = _Tesy.Polygon_height_set
    __swig_getmethods__["height"] = _Tesy.Polygon_height_get
    if _newclass:
        height = _swig_property(_Tesy.Polygon_height_get, _Tesy.Polygon_height_set)
    __swig_setmethods__["label"] = _Tesy.Polygon_label_set
    __swig_getmethods__["label"] = _Tesy.Polygon_label_get
    if _newclass:
        label = _swig_property(_Tesy.Polygon_label_get, _Tesy.Polygon_label_set)
    __swig_setmethods__["segments"] = _Tesy.Polygon_segments_set
    __swig_getmethods__["segments"] = _Tesy.Polygon_segments_get
    if _newclass:
        segments = _swig_property(_Tesy.Polygon_segments_get, _Tesy.Polygon_segments_set)
    __swig_setmethods__["corners"] = _Tesy.Polygon_corners_set
    __swig_getmethods__["corners"] = _Tesy.Polygon_corners_get
    if _newclass:
        corners = _swig_property(_Tesy.Polygon_corners_get, _Tesy.Polygon_corners_set)

    def __init__(self, *args):
        this = _Tesy.new_Polygon(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def boundaryDist(self, p):
        return _Tesy.Polygon_boundaryDist(self, p)

    def boundingBoxCoords(self):
        return _Tesy.Polygon_boundingBoxCoords(self)

    def normalizedBoundingBoxCoords(self):
        return _Tesy.Polygon_normalizedBoundingBoxCoords(self)
    __swig_destroy__ = _Tesy.delete_Polygon
    __del__ = lambda self: None
Polygon_swigregister = _Tesy.Polygon_swigregister
Polygon_swigregister(Polygon)

class Relationship(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Relationship, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Relationship, name)
    __repr__ = _swig_repr
    __swig_setmethods__["label"] = _Tesy.Relationship_label_set
    __swig_getmethods__["label"] = _Tesy.Relationship_label_get
    if _newclass:
        label = _swig_property(_Tesy.Relationship_label_get, _Tesy.Relationship_label_set)
    __swig_setmethods__["cornerRel"] = _Tesy.Relationship_cornerRel_set
    __swig_getmethods__["cornerRel"] = _Tesy.Relationship_cornerRel_get
    if _newclass:
        cornerRel = _swig_property(_Tesy.Relationship_cornerRel_get, _Tesy.Relationship_cornerRel_set)
    __swig_setmethods__["segmentRel"] = _Tesy.Relationship_segmentRel_set
    __swig_getmethods__["segmentRel"] = _Tesy.Relationship_segmentRel_get
    if _newclass:
        segmentRel = _swig_property(_Tesy.Relationship_segmentRel_get, _Tesy.Relationship_segmentRel_set)
    __swig_setmethods__["polyRel"] = _Tesy.Relationship_polyRel_set
    __swig_getmethods__["polyRel"] = _Tesy.Relationship_polyRel_get
    if _newclass:
        polyRel = _swig_property(_Tesy.Relationship_polyRel_get, _Tesy.Relationship_polyRel_set)

    def __init__(self, *args):
        this = _Tesy.new_Relationship(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def to_String(self):
        return _Tesy.Relationship_to_String(self)
    __swig_destroy__ = _Tesy.delete_Relationship
    __del__ = lambda self: None
Relationship_swigregister = _Tesy.Relationship_swigregister
Relationship_swigregister(Relationship)

class Scene(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Scene, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Scene, name)
    __repr__ = _swig_repr
    __swig_setmethods__["polygons"] = _Tesy.Scene_polygons_set
    __swig_getmethods__["polygons"] = _Tesy.Scene_polygons_get
    if _newclass:
        polygons = _swig_property(_Tesy.Scene_polygons_get, _Tesy.Scene_polygons_set)
    __swig_setmethods__["rel"] = _Tesy.Scene_rel_set
    __swig_getmethods__["rel"] = _Tesy.Scene_rel_get
    if _newclass:
        rel = _swig_property(_Tesy.Scene_rel_get, _Tesy.Scene_rel_set)
    __swig_setmethods__["label"] = _Tesy.Scene_label_set
    __swig_getmethods__["label"] = _Tesy.Scene_label_get
    if _newclass:
        label = _swig_property(_Tesy.Scene_label_get, _Tesy.Scene_label_set)

    def __init__(self, *args):
        this = _Tesy.new_Scene(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def addPolygon(self, poly):
        return _Tesy.Scene_addPolygon(self, poly)

    def relationship(self, *args):
        return _Tesy.Scene_relationship(self, *args)

    def calculateRelationshipsVoid(self):
        return _Tesy.Scene_calculateRelationshipsVoid(self)

    def calculateRelationships(self, polyMain):
        return _Tesy.Scene_calculateRelationships(self, polyMain)
    __swig_destroy__ = _Tesy.delete_Scene
    __del__ = lambda self: None
Scene_swigregister = _Tesy.Scene_swigregister
Scene_swigregister(Scene)

class SimilarityMeasures(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SimilarityMeasures, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SimilarityMeasures, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _Tesy.new_SimilarityMeasures()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def shapeSimilarity(self, p1, p2):
        return _Tesy.SimilarityMeasures_shapeSimilarity(self, p1, p2)

    def pointSimilarity(self, r1, r2):
        return _Tesy.SimilarityMeasures_pointSimilarity(self, r1, r2)

    def similarity(self, *args):
        return _Tesy.SimilarityMeasures_similarity(self, *args)
    __swig_destroy__ = _Tesy.delete_SimilarityMeasures
    __del__ = lambda self: None
SimilarityMeasures_swigregister = _Tesy.SimilarityMeasures_swigregister
SimilarityMeasures_swigregister(SimilarityMeasures)

class ElemRelationship(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ElemRelationship, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ElemRelationship, name)
    __repr__ = _swig_repr
    __swig_setmethods__["label"] = _Tesy.ElemRelationship_label_set
    __swig_getmethods__["label"] = _Tesy.ElemRelationship_label_get
    if _newclass:
        label = _swig_property(_Tesy.ElemRelationship_label_get, _Tesy.ElemRelationship_label_set)
    __swig_setmethods__["rel"] = _Tesy.ElemRelationship_rel_set
    __swig_getmethods__["rel"] = _Tesy.ElemRelationship_rel_get
    if _newclass:
        rel = _swig_property(_Tesy.ElemRelationship_rel_get, _Tesy.ElemRelationship_rel_set)

    def __init__(self, *args):
        this = _Tesy.new_ElemRelationship(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Tesy.delete_ElemRelationship
    __del__ = lambda self: None
ElemRelationship_swigregister = _Tesy.ElemRelationship_swigregister
ElemRelationship_swigregister(ElemRelationship)

class PolyRelationship(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PolyRelationship, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PolyRelationship, name)
    __repr__ = _swig_repr
    __swig_setmethods__["label"] = _Tesy.PolyRelationship_label_set
    __swig_getmethods__["label"] = _Tesy.PolyRelationship_label_get
    if _newclass:
        label = _swig_property(_Tesy.PolyRelationship_label_get, _Tesy.PolyRelationship_label_set)
    __swig_setmethods__["lowLeft"] = _Tesy.PolyRelationship_lowLeft_set
    __swig_getmethods__["lowLeft"] = _Tesy.PolyRelationship_lowLeft_get
    if _newclass:
        lowLeft = _swig_property(_Tesy.PolyRelationship_lowLeft_get, _Tesy.PolyRelationship_lowLeft_set)
    __swig_setmethods__["upLeft"] = _Tesy.PolyRelationship_upLeft_set
    __swig_getmethods__["upLeft"] = _Tesy.PolyRelationship_upLeft_get
    if _newclass:
        upLeft = _swig_property(_Tesy.PolyRelationship_upLeft_get, _Tesy.PolyRelationship_upLeft_set)
    __swig_setmethods__["upRight"] = _Tesy.PolyRelationship_upRight_set
    __swig_getmethods__["upRight"] = _Tesy.PolyRelationship_upRight_get
    if _newclass:
        upRight = _swig_property(_Tesy.PolyRelationship_upRight_get, _Tesy.PolyRelationship_upRight_set)
    __swig_setmethods__["lowRight"] = _Tesy.PolyRelationship_lowRight_set
    __swig_getmethods__["lowRight"] = _Tesy.PolyRelationship_lowRight_get
    if _newclass:
        lowRight = _swig_property(_Tesy.PolyRelationship_lowRight_get, _Tesy.PolyRelationship_lowRight_set)
    __swig_setmethods__["center"] = _Tesy.PolyRelationship_center_set
    __swig_getmethods__["center"] = _Tesy.PolyRelationship_center_get
    if _newclass:
        center = _swig_property(_Tesy.PolyRelationship_center_get, _Tesy.PolyRelationship_center_set)

    def __init__(self, *args):
        this = _Tesy.new_PolyRelationship(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Tesy.delete_PolyRelationship
    __del__ = lambda self: None
PolyRelationship_swigregister = _Tesy.PolyRelationship_swigregister
PolyRelationship_swigregister(PolyRelationship)

# This file is compatible with both classic and new-style classes.


