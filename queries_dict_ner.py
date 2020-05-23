query_4 = """

# toutes les valeurs de la fiche œuvres de cette œuvre.
{
  nodeById(id: "_") {
    ... on NodeOeuvre {
      title
      absolutePath
      fieldUrlAlias
      fieldTitreDeMediation
      fieldSousTitreDeMediation
      fieldOeuvreAuteurs {
        entity {
          fieldAuteurAuteur {
            entity {
              name
              fieldPipDateNaissance {
                startYear
              }
              fieldPipLieuNaissance
              fieldPipDateDeces {
                startYear
              }
               fieldLieuDeces
            }
          }
          fieldAuteurFonction {
            entity {
              name
            }
          }

        }
      }
      fieldVisuelsPrincipals {
        entity {
          name
          vignette
          publicUrl
        }
      }
      fieldDateProduction {
        startPrecision
        startYear
        startMonth
        startDay
        sort
        endPrecision
        endYear
        endMonth
        endDay
        century
      }
      fieldOeuvreSiecle {
         entity {
          name
        }
      }
      fieldOeuvreTypesObjet {
        entity {
          name
          fieldLrefAdlib
        }
      }
      fieldDenominations {
        entity {
          name
        }
      }
      fieldMateriauxTechnique{
        entity {
          name
        }
      }
      fieldOeuvreDimensions {
        entity {
          fieldDimensionPartie {
            entity {
              name
            }
          }
          fieldDimensionType {
            entity {
              name
            }
          }
          fieldDimensionValeur
          fieldDimensionUnite {
           entity {
              name
            }
          }
        }
      }
      fieldOeuvreInscriptions{
        entity {
          fieldInscriptionType {
            entity {
              name
            }
          }
          fieldInscriptionMarque {
            value
          }
          fieldInscriptionEcriture {
            entity {
              name
            }
          }
        }
      }
      fieldOeuvreDescriptionIcono {
        value
      }
      fieldCommentaireHistorique {
        value

      }
      fieldOeuvreThemeRepresente     {
        entity {
          name
        }
      }
      fieldLieuxConcernes {
        entity {
          name
        }
      }
      fieldModaliteAcquisition {
        entity {
          name
        }
      }
      fieldDonateurs {
        entity {
          name
        }
      }
      fieldDateAcquisition {
        startPrecision
        startYear
        startMonth
        startDay
        sort
        endPrecision
        endYear
        endMonth
        endDay
        century
      }
      fieldOeuvreNumInventaire
      fieldOeuvreStyleMouvement {
        entity {
          name
        }
      }
      fieldMusee {
        entity {
          name
        }
      }
      fieldOeuvreExpose {
        entity {
          name
        }
      }
      fieldOeuvreAudios {
        entity {
          fieldMediaFile {
            entity {
              url
              uri {
                value
                url
              }
            }
          }
        }
      }
      fieldOeuvreVideos {
        entity {
          fieldMediaVideoEmbedField
        }
      }
      fieldHdVisuel {
        entity {
          fieldMediaImage {
            entity {
              url
            }
          }
        }
      }
    }
  }
}

"""
# Search in field lieuxConcernes (locations) 
query_search = """


{
  nodeQuery(filter: {conditions: [{field: "field_lieux_concernes.entity.name", value: "Whatlookingfor", operator: LIKE}{field: "type", value: "oeuvre"} {field: "field_visuels_principals", operator: IS_NOT_NULL}]}) {
    count
    entities {
      entityId
      entityBundle
      entityLabel
      ... on NodeOeuvre {
        fieldLrefAdlib
        absolutePath
      }
    }
  }
}

""" 
# Search in field iconography 
_ = """



{
  nodeQuery(filter: {conditions: [{field: "field_oeuvre_description_icono", value: "Whatlookingfor", operator: LIKE}{field: "type", value: "oeuvre"} {field: "field_visuels_principals", operator: IS_NOT_NULL}]}) {
    count
    entities {
      entityId
      entityBundle
      entityLabel
      ... on NodeOeuvre {
        fieldLrefAdlib
        absolutePath
      }
    }
  }
}

"""


dic_ner = {"Place Vendôme":174265,
"Cour des Comptes":181571,
"Couvent des Feuillants":723300,
"Fontaine des Innocents":700218,
"Fontaine du Palmier":737325 ,
"Jardin des Tuileries":366916,
"Palais du Louvre":97010,
"Palais Royal":86293,
"Place Dauphine":131874,
"Place des Victoires":355207,
"Pont des Arts":153073,
"Pont Neuf":137377,
"Pont Royal":273808,
"Galerie Vivienne":766266,
"Saint-Nicolas-des-Champs":117852,
"Carreau du Temple":771621,
"Bibliothèque de l'Arsenal":724155,
"Saint-Gervais-Saint-Protais":153206,
"Hôtel de Ville de Paris":88021,
"Pont Marie":152952,
"Tour Saint-Jacques":171521,
"Arènes de Lutèce":95376,
"Bibliothèque Sainte-Geneviève":81426,
"Palais des Thermes":153222,
"Jardin des plantes":174510,
"Fontaine Médicis":769515,
"Fontaine Saint-Michel":701112,
"Palais de l'Institut":160700,
"Palais du Luxembourg":647123,
"Pont Alexandre-III":702978,
"Pont de la Concorde":171508,
"Pont d'Iéna":587718,
"Tour Eiffel":154190,
"Arc de Triomphe":353311,
"Parc Monceau":491124,
"Château de Vincennes":755262,
"Cimetière de Picpus":152987,
"Notre-Dame de Paris":360775,
"Château de Versailles":348820}


# query_search = """


# # field_oeuvre_types_objet.entity.field_lref_adlib

# {
#   nodeQuery(filter: {conditions: {field: "field_lieux_concernes.entity.name", value: "_", operator: LIKE} }) {
#     count
#     entities {
#       entityId
#       entityBundle
#       entityLabel
#       ... on NodeOeuvre {
#         fieldLrefAdlib
#         absolutePath
#       }
#     }
#   }
# }

# """ 


# field_oeuvre_types_objet.entity.field_lref_adlib

# {
#   nodeQuery(filter: {conditions: {field: "field_lieux_concernes.entity.name", value: "%13e%arrondissement%", operator: LIKE}}) {
#     count
#     entities {
#       entityId
#       entityBundle
#       entityLabel
#       ... on NodeOeuvre {
#         fieldLrefAdlib
#         absolutePath
#       }
#     }
#   }
# }




# # field_oeuvre_types_objet.entity.field_lref_adlib
# # NodeOeuvre.
# {
#   nodeQuery(filter: {conditions: [{field: "field_lieux_concernes.entity.name", value: "%notre%dame%", operator: LIKE}{field: "type", value: "oeuvre"} {field: "field_visuels_principals", operator: IS_NOT_NULL}]}) {
#     count
#     entities {
#       entityId
#       entityBundle
#       entityLabel
#       ... on NodeOeuvre {
#         fieldLrefAdlib
#         absolutePath
#       }
#     }
#   }
# }

# """