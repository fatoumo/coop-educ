import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(20, 12))
ax.set_xlim(0, 20)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(10, 11, 'Business Model Canvas - Alternance IT',
        ha='center', va='center', fontsize=28, fontweight='bold', color='#1971c2')

# Define colors for each section
colors = {
    'partners': '#e3f2fd',
    'activities': '#e8f5e9',
    'value': '#ffebee',
    'relations': '#fff3e0',
    'segments': '#f3e5f5',
    'resources': '#e0f2f1',
    'channels': '#ede7f6',
    'costs': '#ffcdd2',
    'revenue': '#c8e6c9'
}

edge_colors = {
    'partners': '#1e88e5',
    'activities': '#43a047',
    'value': '#e53935',
    'relations': '#fb8c00',
    'segments': '#8e24aa',
    'resources': '#00897b',
    'channels': '#5e35b1',
    'costs': '#c62828',
    'revenue': '#2e7d32'
}

# Row 1 - Top boxes (y: 7-10)
boxes_row1 = [
    {'x': 0.5, 'y': 7, 'w': 3.5, 'h': 3.5, 'color': 'partners', 'title': 'Partenaires Clés',
     'items': ['• CFA CESI/Simplon', '• OPCO 2i', '• Région Occitanie', '• GE employeur']},
    {'x': 4.5, 'y': 7, 'w': 3.5, 'h': 3.5, 'color': 'activities', 'title': 'Activités Clés',
     'items': ['• Matching alternants', '• Formation tuteurs', '• Suivi pédagogique', '• Plateforme SaaS']},
    {'x': 8.5, 'y': 7, 'w': 3.5, 'h': 3.5, 'color': 'value', 'title': 'Proposition Valeur',
     'items': ['• 1ère XP garantie', '• 0€ reste à charge', '• Remplacement 3 mois', '• Accompagnement intensif']},
    {'x': 12.5, 'y': 7, 'w': 3.5, 'h': 3.5, 'color': 'relations', 'title': 'Relation Client',
     'items': ['• Account manager', '• Hotline tuteurs', '• Dashboard online', '• Communauté']},
    {'x': 16.5, 'y': 7, 'w': 3.5, 'h': 3.5, 'color': 'segments', 'title': 'Segments Clients',
     'items': ['• PME Tech 10-50', '• Startups série A', '• ESN régionales', '• Reconversions IT']}
]

# Row 2 - Middle boxes (y: 3.5-6.5)
boxes_row2 = [
    {'x': 0.5, 'y': 3.5, 'w': 3.5, 'h': 3, 'color': 'resources', 'title': 'Ressources Clés',
     'items': ['• Équipe 3 personnes', '• Plateforme tech', '• Réseau entreprises', '• Agrément CFA']},
    {'x': 4.5, 'y': 3.5, 'w': 3.5, 'h': 3, 'color': 'channels', 'title': 'Canaux',
     'items': ['• Direct B2B', '• Partenariats CFA', '• Prescripteurs', '• Events tech']}
]

# Row 3 - Bottom boxes (y: 0.5-3)
boxes_row3 = [
    {'x': 0.5, 'y': 0.5, 'w': 7.5, 'h': 2.5, 'color': 'costs', 'title': 'Structure Coûts',
     'items': ['• Salaires alternants 85%', '• Structure 10%', '• Tech 5%']},
    {'x': 8.5, 'y': 0.5, 'w': 11.5, 'h': 2.5, 'color': 'revenue', 'title': 'Sources Revenus',
     'items': ['• Aides publiques 70%', '• Services B2B 20%', '• SaaS 10%']}
]

def draw_box(box_info):
    rect = FancyBboxPatch(
        (box_info['x'], box_info['y']),
        box_info['w'],
        box_info['h'],
        boxstyle="round,pad=0.05",
        edgecolor=edge_colors[box_info['color']],
        facecolor=colors[box_info['color']],
        linewidth=2.5
    )
    ax.add_patch(rect)

    # Title
    ax.text(box_info['x'] + box_info['w']/2,
            box_info['y'] + box_info['h'] - 0.3,
            box_info['title'],
            ha='center', va='top', fontsize=14, fontweight='bold',
            color=edge_colors[box_info['color']])

    # Items
    y_pos = box_info['y'] + box_info['h'] - 0.7
    for item in box_info['items']:
        ax.text(box_info['x'] + 0.15,
                y_pos,
                item,
                ha='left', va='top', fontsize=11,
                color='#333333')
        y_pos -= 0.45

# Draw all boxes
for box in boxes_row1:
    draw_box(box)

for box in boxes_row2:
    draw_box(box)

for box in boxes_row3:
    draw_box(box)

plt.tight_layout()
plt.savefig('business-model-canvas.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Business Model Canvas image created successfully!")
plt.close()
