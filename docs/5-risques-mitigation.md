# 5. Gestion des risques & Mitigation

## Matrice des risques

```mermaid
graph TD
    R[RISQUES CRITIQUES]
    
    R --> J[Juridiques<br/>Impact: Fatal]
    R --> F[Financiers<br/>Impact: Élevé]
    R --> O[Opérationnels<br/>Impact: Moyen]
    R --> C[Commerciaux<br/>Impact: Élevé]
    
    J --> J1[Non-conformité tuteur<br/>Prob: 30%]
    J --> J2[Facturation alternants<br/>Prob: 0%]
    J --> J3[Accident sans DUER<br/>Prob: 10%]
    
    F --> F1[Trésorerie T2<br/>Prob: 60%]
    F --> F2[Suppression aides<br/>Prob: 20%]
    F --> F3[Impayés clients<br/>Prob: 30%]
    
    O --> O1[Turn-over alternants<br/>Prob: 40%]
    O --> O2[Rupture contrats<br/>Prob: 25%]
    O --> O3[Qualité formation<br/>Prob: 20%]
    
    C --> C1[Pas de clients B2B<br/>Prob: 40%]
    C --> C2[Concurrence CFA<br/>Prob: 50%]
    
    style J fill:#f44336
    style F fill:#ff9800
    style C fill:#ff9800
```

## Plans de mitigation

### 🔴 Risques juridiques (Priorité 1)

| Risque | Mitigation | Coût | Responsable |
|--------|------------|------|-------------|
| Non-conformité tuteur | • Formation obligatoire tuteurs<br/>• Checklist hebdo supervision<br/>• Audit trimestriel DREETS | 2k€/an | COO |
| Facturation interdite | • ZÉRO frais alternants<br/>• Audit tous contrats<br/>• Formation équipe | 0€ | CEO |
| Accident/DUER | • DUER jour 1<br/>• MAJ trimestrielle<br/>• Formation sécurité | 1k€ | COO |
| Responsabilité dirigeants | • RCMS 5k€/an<br/>• Pas de garantie perso<br/>• GE phase 1 | 5k€/an | CEO |

### 🟠 Risques financiers (Priorité 2)

```mermaid
graph LR
    TRESO[Trésorerie tendue] --> SOL1[Ligne crédit 20k€]
    TRESO --> SOL2[Capital initial 30k€]
    TRESO --> SOL3[Facturation anticipée]
    
    AIDES[Baisse aides] --> DIV1[70% revenus B2B année 3]
    AIDES --> DIV2[Multi-OPCO]
    AIDES --> DIV3[Marge unitaire positive]
    
    IMPAYES[Impayés] --> PRO1[Acompte 30%]
    IMPAYES --> PRO2[Contrats courts 3 mois]
    IMPAYES --> PRO3[Assurance crédit]
```

### 🟡 Risques opérationnels (Priorité 3)

| Problème | Indicateur alerte | Action corrective |
|----------|------------------|-------------------|
| Turn-over alternants | > 20% ruptures | • Sélection renforcée<br/>• Mentorat intensifié mois 1-3 |
| Qualité formation | NPS < 7/10 | • Audit CFA partenaire<br/>• Formation tuteurs |
| Charge admin | > 0.5 ETP/10 alt | • Automatisation max<br/>• Externalisation compta |
| Matching entreprises | < 70% placement | • Élargir réseau<br/>• Pré-formation candidats |

### 🟢 Risques commerciaux (Priorité 4)

```mermaid
graph TD
    COM[Risque commercial]
    
    COM --> DIFF[Différenciation faible]
    COM --> ACQU[Coût acquisition élevé]
    
    DIFF --> D1[USP: Reconversion garantie]
    DIFF --> D2[100 premiers jours intensifs]
    DIFF --> D3[Réseau alumni actif]
    
    ACQU --> A1[Partenariats écoles]
    ACQU --> A2[Prescription CFA]
    ACQU --> A3[Success stories]
```

## Scénarios de crise

### Scénario 1 : Contrôle DREETS négatif
1. **J+0** : Avocat spécialisé droit social
2. **J+7** : Plan conformité 30 jours
3. **J+30** : Régularisation complète
4. **Budget** : 10-20k€ provision

### Scénario 2 : Perte CFA partenaire
1. **Backup** : 2 CFA en négociation permanente
2. **Délai bascule** : 3 mois max
3. **Communication** : Transparence alternants/entreprises

### Scénario 3 : Trésorerie -10k€
1. **Levier 1** : Facturation anticipée B2B (5k€)
2. **Levier 2** : Découvert autorisé (10k€)
3. **Levier 3** : Apport personnel dirigeants
4. **Levier 4** : Crowdfunding ESS

## Signaux d'alerte précoce

```mermaid
graph LR
    KPI[KPIs monitoring]
    
    KPI --> K1[Trésorerie < 2 mois]
    KPI --> K2[Pipeline < 5 alternants]
    KPI --> K3[NPS < 7/10]
    KPI --> K4[Ruptures > 15%]
    KPI --> K5[B2B < 30% revenus]
    
    K1 --> A1[ACTION IMMEDIATE]
    K2 --> A2[VIGILANCE]
    K3 --> A2
    K4 --> A1
    K5 --> A2
    
    style A1 fill:#f44336,color:#fff
    style A2 fill:#ff9800
```

## Points de non-retour

- ❌ **Ne JAMAIS** facturer les alternants (pénal)
- ❌ **Ne JAMAIS** signer sans maître d'apprentissage
- ❌ **Ne JAMAIS** garantir personnellement un prêt
- ❌ **Ne JAMAIS** démarrer sans assurances RCMS
- ❌ **Ne JAMAIS** promettre du mentorat 100% IA

## Budget risques année 1

| Poste | Montant | % Budget |
|-------|---------|----------|
| Assurances | 12k€ | 40% |
| Provision juridique | 10k€ | 33% |
| Trésorerie sécurité | 5k€ | 17% |
| Formation conformité | 3k€ | 10% |
| **TOTAL** | **30k€** | **100%** |

## Conclusion

✅ **Projet viable SI** respect strict du cadre légal  
✅ **ROI positif** dès année 2 avec discipline commerciale  
✅ **Protection maximale** via GE → Association → SCIC  
⚠️ **Risque principal** : Dépendance aides publiques → Diversification B2B urgente
