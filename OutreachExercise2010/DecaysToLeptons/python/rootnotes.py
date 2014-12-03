"""
Helper module for displaying ROOT canvases in ipython notebooks

Usage example:
    # Save this file as rootnotes.py to your working directory.
    
    import rootnotes
    c1 = rootnotes.default_canvas()
    fun1 = TF1( 'fun1', 'abs(sin(x)/x)', 0, 10)
    c1.SetGridx()
    c1.SetGridy()
    fun1.Draw()
    c1

More examples: http://mazurov.github.io/webfest2013/

@author alexander.mazurov@cern.ch
@author andrey.ustyuzhanin@cern.ch
@date 2013-08-09
"""

import ROOT
import tempfile

# keep a pointer to the original TCanvas constructor
oldinit = ROOT.TCanvas.__init__

# define a new TCanvas class (inheriting from the original one),
# setting the memory ownership in the constructor
class GarbageCollectionResistentCanvas(ROOT.TCanvas):
  def __init__(self, *args):
    oldinit(self,*args)
    ROOT.SetOwnership(self,False)

# replace the old TCanvas class by the new one
ROOT.TCanvas = GarbageCollectionResistentCanvas

try:
    from IPython.core import display
    from IPython import get_ipython
except ImportError:
    def get_ipython():
        return None


def canvas(name="icanvas", size=(800, 600)):
    """Helper method for creating canvas"""

    # Check if icanvas already exists
    canvas = ROOT.gROOT.FindObject(name)
    assert len(size) == 2
    if not canvas:
        canvas = ROOT.TCanvas(name, name, size[0], size[1])
    #ROOT.SetOwnership(canvas, False)
    return canvas


def default_canvas(name="icanvas", size=(800, 600)):
    """ deprecated """
    return canvas(name=name, size=size)


def _display_canvas(canvas):
    file = tempfile.NamedTemporaryFile(suffix=".png")
    canvas.SaveAs(file.name)
    ip_img = display.Image(filename=file.name, format='png', embed=True)
    return ip_img._repr_png_()


def _display_any(obj):
    file = tempfile.NamedTemporaryFile(suffix=".png",delete=False)
    obj.Draw()
    ROOT.gPad.SaveAs(file.name)
    ip_img = display.Image(filename=file.name, format='png', embed=True)
    return ip_img._repr_png_()

ipy = get_ipython()
if ipy:
    #ROOT.gROOT.SetBatch()
    # register display function with PNG formatter:
    png_formatter = ipy.display_formatter.formatters['image/png'] 

    # Register ROOT types in ipython
    #
    #   In  [1]: canvas = rootnotes.canvas()
    #   In  [2]: canvas
    #   Out [2]: [image will be here]
    png_formatter.for_type(ROOT.TCanvas, _display_canvas)
    png_formatter.for_type(ROOT.TF1, _display_any)
