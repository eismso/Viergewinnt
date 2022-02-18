#Decorator

##Ausgangslage
<p>Ein Programm sendet Benachrichtigungen über wichtige Ereignisse an eine vom Klienten vordefinierte Mailingliste. 
Die Nutzer*innen möchten nun aber nicht nur mehr per E-Mail benachrichtigt werden, sondern auch per SMS, Facebook oder 
über eine Slack Benachrichtigung. Zudem werden die unterschiedlichsten Benachrichtigungs-Kombinationen gewünscht bis hin 
zu Benachrichtigungen auf allen vier Kanälen. All diese potentiellen Benachrichtigungskombinationen rein über die 
Implementierung von Subklassen abzubilden, würde den Rahmen jedes Codes sprengen.<p/>
<p>Bei der Vererbung stößt man hier an seine Grenzen, da diese für diesen Fall zu statisch ist. Außerdem können 
Subklassen nur eine Elternklasse besitze. Eine Klasse kann also nicht die Verhaltensweisen mehrerer Klassen erben.</p>
<p>Daher empfiehlt es sich in diesem Fall anstelle der Vererbung einen Decorator zu verwenden: Mit diesem kann man eine 
Klasse um zusätzliche Funktionalitäten erweitern. Als Real-World Analogie kann das Sich-Warm-Anziehen gesehen werden: 
Wenn es einem kalt ist, zieht man einen Pullover an. Wenn es einem noch immer kalt ist eine Jacke. Wenn es regnet zieht 
man eine Regenjacke darüber. Mit diesen zusätzlichen Schichten erweitert man sein ursprüngliches „Basisrepertoire“. 
Es ist aber auch auf einfache Art und Weise möglich eine Schicht bzw. eine Funktionalität auch wieder wegzulassen.
</p>

##Struktur eines Decorators
<p>Die Komponente stellt die Schnittstelle für Wrapper und dekoriertem Objekt dar. Die konkrete Komponente definiert 
die Klasse von Objekten, die umhüllt werden und definiert das zu verändernde Verhalten. Die Basis-Decorator-Klasse 
verweist auf das zu dekorierende Objekt und delegiert alle Operationen an das umschlossene Objekt. Die konkrete 
Decorator Klasse definiert die zusätzlichen Verhaltensweisen. Der Client kann Komponenten in mehrere, dekorierende 
Schichten einhüllen.
</p>
