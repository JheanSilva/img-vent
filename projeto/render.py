"""Renderiza as folhas DXF em PDF multipagina, PNGs e um contato para conferencia."""
import glob
import os
import ezdxf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy

CFG = Configuration(background_policy=BackgroundPolicy.WHITE)
files = sorted(glob.glob("dxf/PEL-0301_*.dxf"))
os.makedirs("png", exist_ok=True)


def draw(ax, path):
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    ctx = RenderContext(doc)
    ctx.set_current_layout(msp)
    Frontend(ctx, MatplotlibBackend(ax), config=CFG).draw_layout(msp, finalize=True)


with PdfPages("PEL-0301_rev02_MINUTA.pdf") as pdf:
    for p in files:
        fig = plt.figure(figsize=(16.54, 11.69), dpi=200)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_axis_off()
        draw(ax, p)
        pdf.savefig(fig, facecolor="white")
        fig.savefig("png/%s.png" % os.path.basename(p)[:-4], facecolor="white", dpi=110)
        plt.close(fig)
        print("ok", os.path.basename(p))

fig, axes = plt.subplots(3, 4, figsize=(22, 12), dpi=95)
for ax in axes.flat:
    ax.set_axis_off()
for ax, p in zip(axes.flat, files):
    draw(ax, p)
    ax.set_title(os.path.basename(p)[10:-4], fontsize=11)
fig.patch.set_facecolor("white")
fig.tight_layout()
fig.savefig("contato.png", facecolor="white")
print("contato.png gerado")
