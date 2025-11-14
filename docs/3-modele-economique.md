# 3. Modèle économique & Financement

## Sources de revenus - Année 1 (10 alternants)

```mermaid
graph TD
    REV[Revenus totaux<br/>140-250k€] 
    
    REV --> AIDES[Aides publiques<br/>110-190k€]
    REV --> B2B[Revenus propres<br/>30-60k€]
    
    AIDES --> ETAT[État: 50k€<br/>5k€ × 10]
    AIDES --> OPCO[OPCO: 50-120k€<br/>5-12k€ × 10]
    AIDES --> REG[Région: 10-20k€<br/>1-2k€ × 10]
    
    B2B --> RECR[Recrutement<br/>15k€<br/>2.5k€ × 6 placements]
    B2B --> FORM[Formation tuteurs<br/>9k€<br/>1.5k€ × 6 entreprises]
    B2B --> SAAS[Plateforme suivi<br/>12k€<br/>100€/mois × 10]
    
    style B2B fill:#4caf50
    style AIDES fill:#2196f3
```

## Structure de coûts - Année 1

```mermaid
pie title Répartition charges année 1 (162k€)
    "Salaires alternants" : 144
    "Assurances" : 6
    "Juridique/Compta" : 4
    "GE/CFA" : 3
    "Plateforme/Outils" : 3
    "Divers" : 2
```

## Empilement aides par alternant

| Source | Année 1 | Conditions |
|--------|---------|------------|
| État | 5 000€ | < 250 salariés |
| OPCO formation | 5-12 000€ | Selon niveau |
| OPCO équipement | 500€ | Premier matériel |
| Région CFA | 1-2 000€ | Numérique/ZRR |
| **TOTAL** | **11,5-19,5k€** | |

## Offres B2B détaillées

### Pack Recrutement (2 500€)
- Sourcing & présélection (20 candidats → 3 finalistes)
- Tests techniques automatisés
- Garantie remplacement 3 mois

### Pack Formation Tuteurs (1 500€)
- Formation 2 jours maître apprentissage
- Certification conforme réglementation
- Kit outils de suivi + hotline 6 mois

### Plateforme SaaS (99€/mois/alternant)
- Dashboard suivi compétences
- Génération rapports légaux
- Chat support IA intégré
- Matching projets/profils

## Trajectoire financière 3 ans

```mermaid
graph LR
    Y1[Année 1<br/>10 alternants<br/>Équilibre] --> Y2[Année 2<br/>25 alternants<br/>+30-50k€]
    Y2 --> Y3[Année 3 SCIC<br/>50 alternants<br/>+100-200k€]
    
    Y1 --> M1[70% aides<br/>30% B2B]
    Y2 --> M2[50% aides<br/>50% B2B]
    Y3 --> M3[30% aides<br/>70% B2B]
    
    style Y1 fill:#ffeb3b
    style Y2 fill:#8bc34a
    style Y3 fill:#4caf50
```

## Seuil de rentabilité

```mermaid
graph TD
    SR[Seuil rentabilité<br/>7 alternants minimum]
    
    SR --> FIX[Charges fixes<br/>18k€/an]
    SR --> VAR[Marge/alternant<br/>2.5k€]
    
    FIX --> ASS[Assurances: 6k€]
    FIX --> STR[Structure: 12k€]
    
    VAR --> AID[Aides: 15k€]
    VAR --> SAL[- Salaire: 15k€]
    VAR --> B2B[+ B2B: 2.5k€]
```

## Plan trésorerie année 1

| Trim | Entrées | Sorties | Solde | Cumul |
|------|---------|---------|-------|-------|
| T1 | 20k€ (capital) | 15k€ | +5k€ | 5k€ |
| T2 | 35k€ (aides+B2B) | 40k€ | -5k€ | 0k€ |
| T3 | 45k€ | 41k€ | +4k€ | 4k€ |
| T4 | 50k€ | 46k€ | +4k€ | 8k€ |

⚠️ **Point critique T2** : Prévoir ligne de crédit 10k€
