# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Afficher_emprunt.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1236, 465)
        MainWindow.setStyleSheet(u"color :rgb(0, 0, 0);\n"
"font: 87 9pt \"Neue Haas Grotesk Text Pro Blac\";\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.actionAjouter_Etudiant = QAction(MainWindow)
        self.actionAjouter_Etudiant.setObjectName(u"actionAjouter_Etudiant")
        self.actionAjouter_Etudiant.setCheckable(False)
        self.actionEtudiant_Donnee = QAction(MainWindow)
        self.actionEtudiant_Donnee.setObjectName(u"actionEtudiant_Donnee")
        self.actionUne_Section_Donnee = QAction(MainWindow)
        self.actionUne_Section_Donnee.setObjectName(u"actionUne_Section_Donnee")
        self.actionUn_Niveau_Donnee = QAction(MainWindow)
        self.actionUn_Niveau_Donnee.setObjectName(u"actionUn_Niveau_Donnee")
        self.actionSection_et_Niveau = QAction(MainWindow)
        self.actionSection_et_Niveau.setObjectName(u"actionSection_et_Niveau")
        self.actionTel = QAction(MainWindow)
        self.actionTel.setObjectName(u"actionTel")
        self.actionMail = QAction(MainWindow)
        self.actionMail.setObjectName(u"actionMail")
        self.actionAdresse = QAction(MainWindow)
        self.actionAdresse.setObjectName(u"actionAdresse")
        self.actionContenue_du_dictionnaire_Etudiant = QAction(MainWindow)
        self.actionContenue_du_dictionnaire_Etudiant.setObjectName(u"actionContenue_du_dictionnaire_Etudiant")
        self.actionRecherche_par_numero_inscription = QAction(MainWindow)
        self.actionRecherche_par_numero_inscription.setObjectName(u"actionRecherche_par_numero_inscription")
        self.actionRecherche_par_section = QAction(MainWindow)
        self.actionRecherche_par_section.setObjectName(u"actionRecherche_par_section")
        self.actionRecherche_par_section_et_Niveau = QAction(MainWindow)
        self.actionRecherche_par_section_et_Niveau.setObjectName(u"actionRecherche_par_section_et_Niveau")
        self.actionRecherche_par_Niveau = QAction(MainWindow)
        self.actionRecherche_par_Niveau.setObjectName(u"actionRecherche_par_Niveau")
        self.actionAjouter_un_nouvel_Livre = QAction(MainWindow)
        self.actionAjouter_un_nouvel_Livre.setObjectName(u"actionAjouter_un_nouvel_Livre")
        self.actionModifier_nombre_d_exemplaires_d_un_Livre = QAction(MainWindow)
        self.actionModifier_nombre_d_exemplaires_d_un_Livre.setObjectName(u"actionModifier_nombre_d_exemplaires_d_un_Livre")
        self.actionLivre_donnee = QAction(MainWindow)
        self.actionLivre_donnee.setObjectName(u"actionLivre_donnee")
        self.actionLivres_d_un_auteur = QAction(MainWindow)
        self.actionLivres_d_un_auteur.setObjectName(u"actionLivres_d_un_auteur")
        self.actionLivres_d_une_annee_donnee = QAction(MainWindow)
        self.actionLivres_d_une_annee_donnee.setObjectName(u"actionLivres_d_une_annee_donnee")
        self.actionContenue_du_dictionnaire_livre = QAction(MainWindow)
        self.actionContenue_du_dictionnaire_livre.setObjectName(u"actionContenue_du_dictionnaire_livre")
        self.actionRecherche_par_Referance = QAction(MainWindow)
        self.actionRecherche_par_Referance.setObjectName(u"actionRecherche_par_Referance")
        self.actionRecherche_par_titre = QAction(MainWindow)
        self.actionRecherche_par_titre.setObjectName(u"actionRecherche_par_titre")
        self.actionRecherche_par_annee_edition_donne = QAction(MainWindow)
        self.actionRecherche_par_annee_edition_donne.setObjectName(u"actionRecherche_par_annee_edition_donne")
        self.actionRecherche_et_Affichage_des_livres_par_ordre_alphabetique = QAction(MainWindow)
        self.actionRecherche_et_Affichage_des_livres_par_ordre_alphabetique.setObjectName(u"actionRecherche_et_Affichage_des_livres_par_ordre_alphabetique")
        self.actionAjouter_un_nouvel_emprunt = QAction(MainWindow)
        self.actionAjouter_un_nouvel_emprunt.setObjectName(u"actionAjouter_un_nouvel_emprunt")
        self.actionRetour_d_un_emprunt = QAction(MainWindow)
        self.actionRetour_d_un_emprunt.setObjectName(u"actionRetour_d_un_emprunt")
        self.actionSupprimer_d_un_emprunt = QAction(MainWindow)
        self.actionSupprimer_d_un_emprunt.setObjectName(u"actionSupprimer_d_un_emprunt")
        self.actionDate_emprunt = QAction(MainWindow)
        self.actionDate_emprunt.setObjectName(u"actionDate_emprunt")
        self.actionDate_Retour = QAction(MainWindow)
        self.actionDate_Retour.setObjectName(u"actionDate_Retour")
        self.actionContenu_du_dictionnaire_emprunt = QAction(MainWindow)
        self.actionContenu_du_dictionnaire_emprunt.setObjectName(u"actionContenu_du_dictionnaire_emprunt")
        self.actionRecherche_emprunt_par_livre = QAction(MainWindow)
        self.actionRecherche_emprunt_par_livre.setObjectName(u"actionRecherche_emprunt_par_livre")
        self.actionRecherche_emprunt_par_etudiant = QAction(MainWindow)
        self.actionRecherche_emprunt_par_etudiant.setObjectName(u"actionRecherche_emprunt_par_etudiant")
        self.actionRecherche_livres_empruntee_a_une_date_donnee = QAction(MainWindow)
        self.actionRecherche_livres_empruntee_a_une_date_donnee.setObjectName(u"actionRecherche_livres_empruntee_a_une_date_donnee")
        self.actionRecherche_livres_retournee_a_une_date_donne = QAction(MainWindow)
        self.actionRecherche_livres_retournee_a_une_date_donne.setObjectName(u"actionRecherche_livres_retournee_a_une_date_donne")
        self.actionRecherche_livres_empruntee_entre_2_dates_donnee = QAction(MainWindow)
        self.actionRecherche_livres_empruntee_entre_2_dates_donnee.setObjectName(u"actionRecherche_livres_empruntee_entre_2_dates_donnee")
        self.actionRecherche_livres_retournee_entre_2_date_donne = QAction(MainWindow)
        self.actionRecherche_livres_retournee_entre_2_date_donne.setObjectName(u"actionRecherche_livres_retournee_entre_2_date_donne")
        self.actionSupprimer_Etudiant = QAction(MainWindow)
        self.actionSupprimer_Etudiant.setObjectName(u"actionSupprimer_Etudiant")
        self.actionModifier_Etudiant = QAction(MainWindow)
        self.actionModifier_Etudiant.setObjectName(u"actionModifier_Etudiant")
        self.actionMenu_Acceuil = QAction(MainWindow)
        self.actionMenu_Acceuil.setObjectName(u"actionMenu_Acceuil")
        self.actionRecuperation_des_donnee = QAction(MainWindow)
        self.actionRecuperation_des_donnee.setObjectName(u"actionRecuperation_des_donnee")
        self.actionEnregistrer_Ficher_Livres = QAction(MainWindow)
        self.actionEnregistrer_Ficher_Livres.setObjectName(u"actionEnregistrer_Ficher_Livres")
        self.actionEnregistrer_Ficher_Emprunt = QAction(MainWindow)
        self.actionEnregistrer_Ficher_Emprunt.setObjectName(u"actionEnregistrer_Ficher_Emprunt")
        self.actionRecuperer_Ficher_Etudiant = QAction(MainWindow)
        self.actionRecuperer_Ficher_Etudiant.setObjectName(u"actionRecuperer_Ficher_Etudiant")
        self.actionRecuperer_Ficher_Livres = QAction(MainWindow)
        self.actionRecuperer_Ficher_Livres.setObjectName(u"actionRecuperer_Ficher_Livres")
        self.actionRecuperer_Ficher_Emprunt = QAction(MainWindow)
        self.actionRecuperer_Ficher_Emprunt.setObjectName(u"actionRecuperer_Ficher_Emprunt")
        self.actionSupprimer = QAction(MainWindow)
        self.actionSupprimer.setObjectName(u"actionSupprimer")
        self.actionModifier_emprunt = QAction(MainWindow)
        self.actionModifier_emprunt.setObjectName(u"actionModifier_emprunt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 40, 1191, 501))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 10, 251, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1236, 25))
        self.menuAcceuil = QMenu(self.menubar)
        self.menuAcceuil.setObjectName(u"menuAcceuil")
        self.menuMenu_Etudiant = QMenu(self.menubar)
        self.menuMenu_Etudiant.setObjectName(u"menuMenu_Etudiant")
        self.menuMise_a_jour_Etudiant = QMenu(self.menuMenu_Etudiant)
        self.menuMise_a_jour_Etudiant.setObjectName(u"menuMise_a_jour_Etudiant")
        self.menuRecherche_et_Affichage = QMenu(self.menuMenu_Etudiant)
        self.menuRecherche_et_Affichage.setObjectName(u"menuRecherche_et_Affichage")
        self.menuMenu_Gestion_Des_Livres = QMenu(self.menubar)
        self.menuMenu_Gestion_Des_Livres.setObjectName(u"menuMenu_Gestion_Des_Livres")
        self.menuMise_a_jour = QMenu(self.menuMenu_Gestion_Des_Livres)
        self.menuMise_a_jour.setObjectName(u"menuMise_a_jour")
        self.menuRecherche_et_Affichage_2 = QMenu(self.menuMenu_Gestion_Des_Livres)
        self.menuRecherche_et_Affichage_2.setObjectName(u"menuRecherche_et_Affichage_2")
        self.menuGestion_Emprunts = QMenu(self.menubar)
        self.menuGestion_Emprunts.setObjectName(u"menuGestion_Emprunts")
        self.menuMise_a_jour_2 = QMenu(self.menuGestion_Emprunts)
        self.menuMise_a_jour_2.setObjectName(u"menuMise_a_jour_2")
        self.menuRecherche_Affichage = QMenu(self.menuGestion_Emprunts)
        self.menuRecherche_Affichage.setObjectName(u"menuRecherche_Affichage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAcceuil.menuAction())
        self.menubar.addAction(self.menuMenu_Etudiant.menuAction())
        self.menubar.addAction(self.menuMenu_Gestion_Des_Livres.menuAction())
        self.menubar.addAction(self.menuGestion_Emprunts.menuAction())
        self.menuMenu_Etudiant.addAction(self.menuMise_a_jour_Etudiant.menuAction())
        self.menuMenu_Etudiant.addSeparator()
        self.menuMenu_Etudiant.addAction(self.menuRecherche_et_Affichage.menuAction())
        self.menuMise_a_jour_Etudiant.addAction(self.actionAjouter_Etudiant)
        self.menuMise_a_jour_Etudiant.addSeparator()
        self.menuMise_a_jour_Etudiant.addAction(self.actionSupprimer_Etudiant)
        self.menuMise_a_jour_Etudiant.addSeparator()
        self.menuMise_a_jour_Etudiant.addAction(self.actionModifier_Etudiant)
        self.menuRecherche_et_Affichage.addAction(self.actionContenue_du_dictionnaire_Etudiant)
        self.menuRecherche_et_Affichage.addSeparator()
        self.menuRecherche_et_Affichage.addAction(self.actionRecherche_par_numero_inscription)
        self.menuMenu_Gestion_Des_Livres.addAction(self.menuMise_a_jour.menuAction())
        self.menuMenu_Gestion_Des_Livres.addAction(self.menuRecherche_et_Affichage_2.menuAction())
        self.menuMise_a_jour.addAction(self.actionAjouter_un_nouvel_Livre)
        self.menuMise_a_jour.addAction(self.actionSupprimer)
        self.menuMise_a_jour.addAction(self.actionModifier_nombre_d_exemplaires_d_un_Livre)
        self.menuRecherche_et_Affichage_2.addAction(self.actionContenue_du_dictionnaire_livre)
        self.menuRecherche_et_Affichage_2.addAction(self.actionRecherche_par_Referance)
        self.menuGestion_Emprunts.addAction(self.menuMise_a_jour_2.menuAction())
        self.menuGestion_Emprunts.addAction(self.menuRecherche_Affichage.menuAction())
        self.menuMise_a_jour_2.addAction(self.actionAjouter_un_nouvel_emprunt)
        self.menuMise_a_jour_2.addAction(self.actionRetour_d_un_emprunt)
        self.menuMise_a_jour_2.addAction(self.actionSupprimer_d_un_emprunt)
        self.menuMise_a_jour_2.addAction(self.actionModifier_emprunt)
        self.menuRecherche_Affichage.addAction(self.actionContenu_du_dictionnaire_emprunt)
        self.menuRecherche_Affichage.addAction(self.actionRecherche_emprunt_par_livre)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAjouter_Etudiant.setText(QCoreApplication.translate("MainWindow", u"Ajouter Etudiant", None))
        self.actionEtudiant_Donnee.setText(QCoreApplication.translate("MainWindow", u"Etudiant Donnee", None))
        self.actionUne_Section_Donnee.setText(QCoreApplication.translate("MainWindow", u"Une Section Donnee", None))
        self.actionUn_Niveau_Donnee.setText(QCoreApplication.translate("MainWindow", u"Un Niveau Donnee", None))
        self.actionSection_et_Niveau.setText(QCoreApplication.translate("MainWindow", u"Section et Niveau", None))
        self.actionTel.setText(QCoreApplication.translate("MainWindow", u"Tel", None))
        self.actionMail.setText(QCoreApplication.translate("MainWindow", u"Mail", None))
        self.actionAdresse.setText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.actionContenue_du_dictionnaire_Etudiant.setText(QCoreApplication.translate("MainWindow", u"Afficher les Etudiants", None))
        self.actionRecherche_par_numero_inscription.setText(QCoreApplication.translate("MainWindow", u"Recherche", None))
        self.actionRecherche_par_section.setText(QCoreApplication.translate("MainWindow", u"Recherche par section", None))
        self.actionRecherche_par_section_et_Niveau.setText(QCoreApplication.translate("MainWindow", u"Recherche par section et Niveau ", None))
        self.actionRecherche_par_Niveau.setText(QCoreApplication.translate("MainWindow", u"Recherche par Niveau", None))
        self.actionAjouter_un_nouvel_Livre.setText(QCoreApplication.translate("MainWindow", u"Ajouter un nouvel Livre", None))
        self.actionModifier_nombre_d_exemplaires_d_un_Livre.setText(QCoreApplication.translate("MainWindow", u"Modifier nombre d exemplaires d un Livre", None))
        self.actionLivre_donnee.setText(QCoreApplication.translate("MainWindow", u"Livre donnee", None))
        self.actionLivres_d_un_auteur.setText(QCoreApplication.translate("MainWindow", u"Livres d un auteur", None))
        self.actionLivres_d_une_annee_donnee.setText(QCoreApplication.translate("MainWindow", u"Livres d une annee donnee", None))
        self.actionContenue_du_dictionnaire_livre.setText(QCoreApplication.translate("MainWindow", u"Afficher les livres", None))
        self.actionRecherche_par_Referance.setText(QCoreApplication.translate("MainWindow", u"Recherche", None))
        self.actionRecherche_par_titre.setText(QCoreApplication.translate("MainWindow", u"Recherche par titre", None))
        self.actionRecherche_par_annee_edition_donne.setText(QCoreApplication.translate("MainWindow", u"Recherche par annee edition donne", None))
        self.actionRecherche_et_Affichage_des_livres_par_ordre_alphabetique.setText(QCoreApplication.translate("MainWindow", u"Recherche et Affichage des livres par ordre alphabetique", None))
        self.actionAjouter_un_nouvel_emprunt.setText(QCoreApplication.translate("MainWindow", u"Ajouter un nouvel emprunt", None))
        self.actionRetour_d_un_emprunt.setText(QCoreApplication.translate("MainWindow", u"Retour d un emprunt", None))
        self.actionSupprimer_d_un_emprunt.setText(QCoreApplication.translate("MainWindow", u"Supprimer d un emprunt", None))
        self.actionDate_emprunt.setText(QCoreApplication.translate("MainWindow", u"Date emprunt", None))
        self.actionDate_Retour.setText(QCoreApplication.translate("MainWindow", u"Date Retour", None))
        self.actionContenu_du_dictionnaire_emprunt.setText(QCoreApplication.translate("MainWindow", u"Afficher les Emprunts", None))
        self.actionRecherche_emprunt_par_livre.setText(QCoreApplication.translate("MainWindow", u"Recherche emprunt ", None))
        self.actionRecherche_emprunt_par_etudiant.setText(QCoreApplication.translate("MainWindow", u"Recherche emprunt par etudiant", None))
        self.actionRecherche_livres_empruntee_a_une_date_donnee.setText(QCoreApplication.translate("MainWindow", u"Recherche livres empruntee a une date donnee", None))
        self.actionRecherche_livres_retournee_a_une_date_donne.setText(QCoreApplication.translate("MainWindow", u"Recherche livres retournee a une date donne", None))
        self.actionRecherche_livres_empruntee_entre_2_dates_donnee.setText(QCoreApplication.translate("MainWindow", u"Recherche livres empruntee entre 2 dates donnee", None))
        self.actionRecherche_livres_retournee_entre_2_date_donne.setText(QCoreApplication.translate("MainWindow", u"Recherche livres retournee entre 2 date donne", None))
        self.actionSupprimer_Etudiant.setText(QCoreApplication.translate("MainWindow", u"Supprimer Etudiant", None))
        self.actionModifier_Etudiant.setText(QCoreApplication.translate("MainWindow", u"Modifier Etudiant", None))
        self.actionMenu_Acceuil.setText(QCoreApplication.translate("MainWindow", u"Menu Acceuil", None))
        self.actionRecuperation_des_donnee.setText(QCoreApplication.translate("MainWindow", u"Recuperer les donnee", None))
        self.actionEnregistrer_Ficher_Livres.setText(QCoreApplication.translate("MainWindow", u"Enregistrer Ficher Livres", None))
        self.actionEnregistrer_Ficher_Emprunt.setText(QCoreApplication.translate("MainWindow", u"Enregistrer Ficher Emprunt", None))
        self.actionRecuperer_Ficher_Etudiant.setText(QCoreApplication.translate("MainWindow", u"Recuperer Ficher Etudiant", None))
        self.actionRecuperer_Ficher_Livres.setText(QCoreApplication.translate("MainWindow", u"Recuperer Ficher Livres", None))
        self.actionRecuperer_Ficher_Emprunt.setText(QCoreApplication.translate("MainWindow", u"Recuperer Ficher Emprunt", None))
        self.actionSupprimer.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actionModifier_emprunt.setText(QCoreApplication.translate("MainWindow", u"Modifier emprunt", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Liste des emprunts", None))
        self.menuAcceuil.setTitle(QCoreApplication.translate("MainWindow", u"Acceuil", None))
        self.menuMenu_Etudiant.setTitle(QCoreApplication.translate("MainWindow", u"Menu Etudiant ", None))
        self.menuMise_a_jour_Etudiant.setTitle(QCoreApplication.translate("MainWindow", u"Mise a jour Etudiant", None))
        self.menuRecherche_et_Affichage.setTitle(QCoreApplication.translate("MainWindow", u"Recherche et Affichage", None))
        self.menuMenu_Gestion_Des_Livres.setTitle(QCoreApplication.translate("MainWindow", u"Menu Gestion Des Livres", None))
        self.menuMise_a_jour.setTitle(QCoreApplication.translate("MainWindow", u"Mise a jour", None))
        self.menuRecherche_et_Affichage_2.setTitle(QCoreApplication.translate("MainWindow", u"Recherche et Affichage", None))
        self.menuGestion_Emprunts.setTitle(QCoreApplication.translate("MainWindow", u"Gestion Emprunts", None))
        self.menuMise_a_jour_2.setTitle(QCoreApplication.translate("MainWindow", u"Mise a jour", None))
        self.menuRecherche_Affichage.setTitle(QCoreApplication.translate("MainWindow", u"Recherche ,Affichage", None))
    # retranslateUi

