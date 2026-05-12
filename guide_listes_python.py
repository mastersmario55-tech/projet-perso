from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm

doc = SimpleDocTemplate("guide_listes_python.pdf", pagesize=A4,
                        leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)

BLEU = colors.HexColor("#2E75B6")
VERT = colors.HexColor("#1F6B2E")
ROUGE = colors.HexColor("#C00000")
DARK = colors.HexColor("#1F1F1F")
GRIS = colors.HexColor("#555555")
CODE_BG = colors.HexColor("#EBF3FB")
JAUNE_BG = colors.HexColor("#FFFDE7")

titre_s = ParagraphStyle('titre', fontSize=24, textColor=BLEU, fontName="Helvetica-Bold", spaceAfter=4, alignment=1)
sous_titre_s = ParagraphStyle('sous_titre', fontSize=12, textColor=GRIS, fontName="Helvetica-Oblique", spaceAfter=20, alignment=1)
h1_s = ParagraphStyle('h1', fontSize=14, textColor=colors.white, fontName="Helvetica-Bold",
                      spaceBefore=14, spaceAfter=8, backColor=BLEU, borderPadding=6)
h2_s = ParagraphStyle('h2', fontSize=11, textColor=BLEU, fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=4)
normal_s = ParagraphStyle('normal', fontSize=10, fontName="Helvetica", spaceAfter=4, leading=15, textColor=DARK)
code_s = ParagraphStyle('code', fontSize=9, fontName="Courier", textColor=BLEU,
                        backColor=CODE_BG, spaceAfter=3, leftIndent=16, borderPadding=5, leading=14)
ok_s = ParagraphStyle('ok', fontSize=10, fontName="Helvetica", textColor=VERT, spaceAfter=3, leftIndent=10)
nok_s = ParagraphStyle('nok', fontSize=10, fontName="Helvetica", textColor=ROUGE, spaceAfter=3, leftIndent=10)
info_s = ParagraphStyle('info', fontSize=10, fontName="Helvetica-Oblique", textColor=GRIS,
                        spaceAfter=6, backColor=JAUNE_BG, borderPadding=6)
warning_s = ParagraphStyle('warning', fontSize=10, fontName="Helvetica-Bold", textColor=ROUGE,
                           spaceAfter=6, backColor=colors.HexColor("#FFF0F0"), borderPadding=6)

def make_table(headers, rows, col_widths):
    data = [headers] + rows
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), BLEU),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [CODE_BG, colors.white]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    return t

def c(text):
    return Paragraph(text, code_s)

story = []

# TITRE
story.append(Spacer(1, 10))
story.append(Paragraph("Les Listes en Python", titre_s))
story.append(Paragraph("Guide complet pour debutant - Cours OpenClassrooms", sous_titre_s))
story.append(HRFlowable(width="100%", thickness=2, color=BLEU))
story.append(Spacer(1, 10))
story.append(Paragraph(
    "Une liste c'est comme un panier de courses : elle peut contenir plusieurs elements "
    "differents en meme temps, et tu peux y ajouter, retirer ou modifier ce que tu veux !",
    info_s))
story.append(Spacer(1, 8))

# SECTION 1
story.append(Paragraph("  1. C'est quoi une liste ?", h1_s))
story.append(Paragraph("Une liste est une variable qui contient plusieurs valeurs entre crochets [ ] :", normal_s))
story.append(c('fruits = ["pomme", "banane", "orange"]'))
story.append(c('nombres = [1, 2, 3, 4, 5]'))
story.append(c('mixte = ["texte", 42, True, 3.14]   # On peut melanger les types !'))
story.append(Spacer(1, 10))

# SECTION 2
story.append(Paragraph("  2. Acceder aux elements - Les indices", h1_s))
story.append(Paragraph("Chaque element a un indice (position). En Python, on commence TOUJOURS a compter a partir de 0 !", normal_s))
story.append(Spacer(1, 6))
story.append(make_table(
    ["Element", "pomme", "banane", "orange"],
    [
        ["Indice normal", "0", "1", "2"],
        ["Indice negatif", "-3", "-2", "-1"],
    ],
    [4*cm, 4*cm, 4*cm, 3.5*cm]
))
story.append(Spacer(1, 8))
story.append(c('fruits = ["pomme", "banane", "orange"]'))
story.append(c('fruits[0]    # "pomme"  -> 1er element'))
story.append(c('fruits[1]    # "banane" -> 2eme element'))
story.append(c('fruits[-1]   # "orange" -> dernier element (indice negatif)'))
story.append(Spacer(1, 6))
story.append(Paragraph("Ca marche aussi avec les chaines de caracteres !", h2_s))
story.append(c('langage = "PYTHON"'))
story.append(c('langage[0]   # "P"'))
story.append(c('langage[2]   # "T"'))
story.append(c('langage[-1]  # "N"'))
story.append(Spacer(1, 10))

# SECTION 3
story.append(Paragraph("  3. Modifier un element", h1_s))
story.append(Paragraph("On utilise l'indice avec l'operateur = :", normal_s))
story.append(c('fruits = ["pomme", "banane", "orange"]'))
story.append(c('fruits[1] = "ananas"   # Remplace "banane" par "ananas"'))
story.append(c('print(fruits)          # ["pomme", "ananas", "orange"]'))
story.append(Spacer(1, 10))

# SECTION 4
story.append(Paragraph("  4. Les methodes essentielles", h1_s))
story.append(Spacer(1, 6))
story.append(make_table(
    ["Methode", "Role", "Exemple", "Resultat"],
    [
        ["append()", "Ajoute a la fin", 'fruits.append("kiwi")', "Ajoute kiwi"],
        ["remove()", "Supprime un element", 'fruits.remove("pomme")', "Retire pomme"],
        ["sort()", "Trie la liste", "fruits.sort()", "Ordre alpha"],
        ["len()", "Longueur de la liste", "len(fruits)", "3"],
        ["extend()", "Ajoute plusieurs elements", 'fruits.extend(["mangue","fraise"])', "Ajoute les 2"],
        ["insert()", "Insere a une position", 'fruits.insert(1, "melon")', "Insere en pos 1"],
        ["pop()", "Supprime le dernier", "fruits.pop()", "Retourne le dernier"],
        ["reverse()", "Inverse l'ordre", "fruits.reverse()", "Ordre inverse"],
        ["count()", "Compte les occurrences", 'fruits.count("pomme")', "Nombre de fois"],
        ["index()", "Donne l'indice", 'fruits.index("banane")', "Retourne indice"],
    ],
    [3*cm, 4*cm, 4.5*cm, 4*cm]
))
story.append(Spacer(1, 10))

# SECTION 5
story.append(Paragraph("  5. Exemple pratique complet", h1_s))
story.append(c('# Creation de la liste'))
story.append(c('fruits = ["pomme", "banane", "orange"]'))
story.append(c(''))
story.append(c('# Ajout d un element'))
story.append(c('fruits.append("kiwi")'))
story.append(c(''))
story.append(c('# Suppression d un element'))
story.append(c('fruits.remove("orange")'))
story.append(c(''))
story.append(c('# Modification du 2eme element (indice 1)'))
story.append(c('fruits[1] = "ananas"'))
story.append(c(''))
story.append(c('# Affichage de la longueur'))
story.append(c('print("La liste contient", len(fruits), "elements.")'))
story.append(c(''))
story.append(c('# Tri et affichage final'))
story.append(c('fruits.sort()'))
story.append(c('print(fruits)   # ["ananas", "kiwi", "pomme"]'))
story.append(Spacer(1, 10))

# SECTION 6
story.append(Paragraph("  6. Ce qu'il faut faire et ne pas faire", h1_s))
story.append(Spacer(1, 6))
story.append(Paragraph("✅  Toujours utiliser des crochets [ ] pour creer une liste", ok_s))
story.append(Paragraph("✅  Separer les elements par des virgules", ok_s))
story.append(Paragraph("✅  Se rappeler que les indices commencent a 0 et non a 1", ok_s))
story.append(Paragraph("✅  Utiliser des commentaires # pour expliquer chaque etape", ok_s))
story.append(Paragraph("✅  Utiliser print() pour verifier le contenu de sa liste", ok_s))
story.append(Spacer(1, 6))
story.append(Paragraph("❌  Ne jamais acceder a un indice qui n'existe pas !", warning_s))
story.append(c('fruits = ["pomme", "banane", "orange"]  # indices : 0, 1, 2'))
story.append(c('fruits[5]   # ❌ IndexError : indice 5 n existe pas !'))
story.append(c('fruits[3]   # ❌ IndexError : indice 3 n existe pas non plus !'))
story.append(Spacer(1, 10))

# SECTION 7
story.append(Paragraph("  7. Vocabulaire cle a retenir", h1_s))
story.append(Spacer(1, 6))
story.append(make_table(
    ["Terme", "Definition"],
    [
        ["Liste", "Variable contenant plusieurs valeurs entre crochets [ ]"],
        ["Indice", "Position d'un element dans la liste (commence a 0)"],
        ["Methode", "Fonction propre a un type (append, remove, sort...)"],
        ["append()", "Ajoute un element a la fin de la liste"],
        ["remove()", "Supprime la premiere occurrence d'un element"],
        ["sort()", "Trie les elements par ordre alphabetique ou numerique"],
        ["len()", "Retourne le nombre d'elements dans la liste"],
        ["IndexError", "Erreur quand on accede a un indice inexistant"],
        ["Indice negatif", "Acceder aux elements depuis la fin (-1 = dernier)"],
    ],
    [4*cm, 11.5*cm]
))

story.append(Spacer(1, 20))
story.append(HRFlowable(width="100%", thickness=1, color=BLEU))
story.append(Paragraph(
    "Les listes sont l'un des outils les plus utilises en Python. Maitrise-les bien !",
    ParagraphStyle('footer', fontSize=10, textColor=BLEU, fontName="Helvetica-Oblique",
                   alignment=1, spaceBefore=8)
))

doc.build(story)
print("PDF cree !")