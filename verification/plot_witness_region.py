"""Plot the exact sufficient witness region for the integer covariance family."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parents[1]
dest=root/'science'/'figures'
dest.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none','svg.hashsalt':'pure-dephasing-region'})
t=np.linspace(7.5,90,600)
boundary=1/15-1/(2*t)
fig,ax=plt.subplots(figsize=(8,4.7),layout='constrained')
fig.patch.set_facecolor('white')
ax.set_facecolor('#f8fafc')
ax.fill_between(t,0,boundary,color='#cfe6f4',label='PPT entanglement certified')
ax.plot(t,boundary,color='#17668a',lw=2,label=r'$\delta+1/(2t)=1/15$')
ax.axhline(1/15,color='#64748b',ls='--',lw=1.1)
ax.scatter([30],[1/30],s=52,color='#ac3d28',zorder=4)
ax.annotate('Exact example\n(t = 30, δ = 1/30)',xy=(30,1/30),xytext=(40,.023),arrowprops={'arrowstyle':'-','color':'#ac3d28'},color='#903322')
ax.text(58,.047,'Certified PPT entanglement',color='#15536c',ha='center',fontsize=10)
ax.text(34,.073,'All displayed parameters preserve PPT',color='#374151',fontsize=10)
ax.text(47,.063,'Witness is inconclusive above the curve',color='#475569',fontsize=9)
ax.set(xlim=(0,90),ylim=(0,.08),xlabel='Dimensionless dephasing time t',ylabel='Added covariance noise δ',title='Bound entanglement from eight vacuum carriers')
ax.spines[['top','right']].set_visible(False)
ax.grid(alpha=.18)
fig.savefig(dest/'witness-region.svg',metadata={'Date':None})
print(dest/'witness-region.svg')
