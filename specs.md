# Cahier des Charges - Bot Discord Daily Digest

## 1. Objectif du Bot
Le bot Discord doit fournir un résumé quotidien des messages postés sur tous les salons d'un serveur, en publiant ce résumé à 21h sur le salon #daily-digest. Le résumé devra être une synthèse des échanges principaux, structurée de manière claire (titres, bullet points).

## 2. Contenu du Résumé
- Synthèse des échanges principaux de tous les salons, avec priorité aux messages ayant reçu le plus de réactions et une évaluation automatisée de la pertinence.
- Récupération de l'historique des messages sur 24 heures tous les jours à 21h.
- Résumé global regroupant tous les salons (plutôt qu'un résumé par salon).
- Style amical et structuration avec titres et bullet points.

## 3. Fréquence de Publication
- Publication du résumé tous les soirs à 21h.

## 4. Salons à Exclure
- Le salon #bienvenue (messages automatiques d'arrivée des utilisateurs) sera exclu.
- Possibilité de modifier la liste des salons exclus à l'avenir.

## 5. Technologie et Bibliothèques
- Langage : Python.
- Bibliothèque Discord : **discord.py**.
- Résumé du contenu : Utilisation des services OpenAI (GPT-3.5 ou GPT-4) avec choix du modèle paramétrable.

## 6. Permissions du Bot
- Droits en lecture sur tous les salons (excepté ceux exclus).
- Droit de publication sur le salon #daily-digest.

## 7. Fonctionnalités de Personnalisation
- Possibilité pour les administrateurs de modifier :
  - L'heure de publication.
  - Les salons à exclure.
  - Le niveau de détail du résumé.

## 8. Gestion des Erreurs
- En cas d'échec de lecture ou de problème avec l'API OpenAI : réessayer 5 fois toutes les 5 minutes.
- Notifier les administrateurs à chaque tentative.

## 9. Journalisation
- Conservation des logs pendant une semaine en local.
- Envoi des logs par mail pour suivi des événements (erreurs, succès de publication).

## 10. Sécurité
- Les clés API (Discord, OpenAI) seront stockées en tant que variables d'environnement sur Azure.

## 11. Commandes d'Administration
- Commandes Discord permettant aux administrateurs d'ajuster certains paramètres du bot (heure de publication, salons exclus, niveau de détail du résumé).

## 12. Surveillance de l'État du Bot
- Pas de fonctionnalité de surveillance de l'état du bot requise pour l'instant.

## 13. Historique des Résumés
- Pas de système d'archivage supplémentaire : les résumés sont disponibles sur le salon #daily-digest.

## 14. Limites du Résumé
- Le résumé pourra être assez détaillé, avec une limite de longueur à déterminer ultérieurement.
