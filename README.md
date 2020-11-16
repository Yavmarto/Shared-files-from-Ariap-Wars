# Shared-files-from-Ariap-Wars

Dit is zijn scripts die gebruikt worden in de game Ariap Wars.

Ariap Wars is een cross platform mobile game gemaakt in Godot (https://godotengine.org/). Het is een soloproject waarbij ik verantwoordelijk ben voor alle onderdelen van het project. Het gaat om een 2D turned based strategy game waarin spelers hun units om de beurt verplaatsen en elkaar aan vallen. De laatste speler die nog units op het veld heeft, wint.

Hierbij moeten veel levels ontwikkeld worden en dat kost veel tijd. Om tijd te besparen had ik bedacht om de levels te bouwen met behulp van PCG in python. In de folder met python scripts zorgt file_creator.py voor het eindproduct waarbij de andere scripts gebruikt worden om een level te genereren (een bestand dat direct in de Godot engine te gebruiken is). De andere files doen het daadwerkelijke genereer werk.

In Ariap Wars is mogelijk om tegen andere mensen te spelen maar ook tegen de AI. De AI moet natuurlijk wel uitdagend genoeg zijn en 'slimme zetten' doen. De AI_Battle_Calculator krijgt een set met moves die mogelijk zijn, en haalt eerst de onnodige en overbodige moves weg. Dan berekent hij wat er gebeurt als hij bepaalde move combinaties doet. Dit kan recursief, dus de AI kan meerdere stappen de diepte in denken. Daarna kan hij de beste move uitvoeren.
