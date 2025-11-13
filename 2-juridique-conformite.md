# 2. Modèle juridique & Conformité

## Choix du contrat : Apprentissage uniquement

```mermaid
graph TD
    CHOIX[Type de contrat] --> APP[Contrat Apprentissage<br/>✓ 5000€ aide État<br/>✓ OPCO finance formation<br/>✓ Exonérations charges]
    CHOIX --> PRO[Contrat Pro<br/>✗ 0€ aide depuis 04/2024<br/>✗ Plus coûteux<br/>✗ Moins flexible]
    
    APP --> SAL[Salaire alternant 21 ans]
    SAL --> Y1[Année 1: 43% SMIC = 775€]
    SAL --> Y2[Année 2: 61% SMIC = 1099€]
    SAL --> Y3[Année 3: 78% SMIC = 1406€]
    
    style APP fill:#4caf50
    style PRO fill:#f44336
```

## Obligations légales NON NÉGOCIABLES

| ⛔ INTERDIT | ✅ OBLIGATOIRE | 🔧 SOLUTION CONFORME |
|-------------|----------------|---------------------|
| Mentorat 100% IA | Maître apprentissage humain | IA en support uniquement |
| Auto-organisation | Subordination employeur | Autonomie encadrée/Agile |
| Frais aux alternants | Gratuité totale formation | Revenus B2B exclusivement |
| Absence supervision | DUER + suivi hebdo | Process documentés |

## Structure juridique optimale

```mermaid
stateDiagram-v2
    [*] --> Association
    Association --> SCIC: Transformation<br/>Vote AG + Agrément<br/>Mois 18-24
    
    Association: Création rapide (500€)
    Association: Dirigeants bénévoles protégés
    Association: Clause transformation SCIC
    Association: Partenariat CFA
    Association: Emploi via GE
    
    SCIC: Capital 5-10k€
    SCIC: Responsabilité limitée
    SCIC: Multi-parties prenantes
    SCIC: IS = 0 si 100% réserves
    SCIC: Emploi direct alternants
```

## Gouvernance SCIC

```mermaid
pie title Répartition droits de vote SCIC
    "Salariés/Fondateurs" : 30
    "Entreprises clientes" : 30
    "Collectivités/CFA" : 20
    "Alternants alumni" : 10
    "Partenaires ESS" : 10
```

## Assurances critiques (12k€/an)

1. **RC Pro** : 2k€/an - Dommages tiers
2. **RCMS** : 3-5k€/an - Protection patrimoine dirigeants ⚠️ CRITIQUE
3. **Cyber** : 2k€/an - Ransomware/RGPD
4. **Mutuelle** : 3-4k€/an - Obligatoire alternants
5. **AGS** : Via URSSAF - Automatique

## Montage avec Groupement d'Employeurs

```mermaid
graph LR
    GE[GE IT Occitanie<br/>Employeur légal] --> A1[Alternant 1]
    GE --> A2[Alternant 2]
    GE --> A3[Alternant 3]
    
    ASSO[Votre Association<br/>Utilisatrice] --> GE
    PME1[PME Cliente 1] --> GE
    PME2[PME Cliente 2] --> GE
    
    GE --> RESP[Responsabilité<br/>employeur]
    ASSO --> COORD[Coordination<br/>pédagogique]
    
    style GE fill:#2196f3
    style RESP fill:#ff9800
```

## Checklist conformité

- [ ] Maître apprentissage désigné (2 ans XP ou diplôme+1an)
- [ ] Ratio 1 maître / 2 apprentis max
- [ ] Formation théorique 25% minimum via CFA Qualiopi
- [ ] DUER rédigé et à jour
- [ ] Visite médicale sous 2 mois
- [ ] Contrats conformes CERFA
- [ ] Zéro facturation alternants
- [ ] Traçabilité supervision hebdo
