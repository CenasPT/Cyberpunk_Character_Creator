from Classes_Cyberpunk import * # Classes do projeto

# Lista de personagens predefinidos
personagens_predefinidos = ["Johnny Silverhand", "Morgan Blackhand", "Alt Cunningham", "Saburo Arasaka", "Adam Smasher", "Rogue Amendiares", "Rache Bartmoss"]
    
# Instanciação de objetos (personagens predefinidos do projeto)
# Personagem Predefinido 1
Johnny=Rockerboy("Johnny Silverhand",10,20)
Johnny.set_cybernetic_implant("Braço cibernético Cromado")
info ="""Johnny Silverhand, nascido Robert John Linder, foi um famoso e influente rockerboy e vocalista da banda Samurai.
Como veterano militar, definiu o movimento rockerboy tal como é conhecido hoje,
destacando-se como a principal figura na luta contra o governo corrupto da NUSA e as megacorporações,
sendo, devido a essa mesma luta, frequentemente descrito como um terrorista.
Apesar do seu carisma e charme, também era conhecido por ser irracional, impulsivo e manipulador.
Silverhand ganhou o seu apelido devido ao braço esquerdo prateado
que foi implantado após perder o seu braço verdadeiro na Segunda Guerra da América Central.
Provavelmente uma das primeiras vítimas de ciberpsicose, tornou-se demasiado temperamental.
É descrito numa entrevista como sendo impulsionado pela sua dedicação e ambiciosidade,
mas, no final do dia, Silverhand é alguém que não se importa muito com as pessoas ao seu redor,
desde que sejam utilizadas para alcançar os seus objetivos.
Eventualmente, Silverhand foi morto por Adam Smasher durante o Holocausto de Night City em 20 de agosto de 2023.
No entanto, a sua consciência foi copiada e armazenada num dispositivo (Relic) após o seu encontro com Smasher, pouco antes da sua morte.
Esta cópia não é a sua consciência real, mas sim uma réplica digital da sua personalidade."""
Johnny.set_info_adicional(info)
# Personagem Predefinido 2
Morgan=Solo("Morgan Blackhand",10,20)
Morgan.set_cybernetic_implant("Braço cibernético Cromado")
info ="""Morgan Blackhand possui um braço cibernético anodizado preto-cromado.
Ele é caracterizado pelo facto de ser um pragmático.
Blackhand consegue sobreviver porque é astuto e está constantemente a zelar pelos seus próprios interesses.
A sua reputação como um dos melhores solos deve-se, em parte, ao facto de conseguir capturar os seus alvos ainda vivos,
em vez de simplesmente os eliminar.
Basicamente, Blackhand é considerado o "Solo dos Solos", com anos de experiência e missões bem-sucedidas no seu currículo.
Morgan trabalha para a oferta mais alta,
não tem agenda própria e não aspira a ser mais do que aquilo que já é.
Simplesmente aceita os trabalhos que lhe são atribuídos e executa-os da forma que considera mais adequada."""
Morgan.set_info_adicional(info)
# Personagem Predefinido 3
Alt=Netrunner("Alt Cunningham",10,20)
Alt.set_cybernetic_implant("Ligações de Interface")
info ="""Altiera Cunningham, mais conhecida como Alt,
foi a melhor Netrunner de Night City durante as décadas de 2000 e 2010.
Descrita como uma mulher bonita e talentosa,
trabalhou para a Corporação ITS e foi a criadora do infame programa Soulkiller.
Cunningham era a namorada do famoso rockerboy Johnny Silverhand.
No entanto, a sua vida mudou completamente quando foi raptada pela Corporação Arasaka,
que a usou para criar uma outra versão do programa Soulkiller para a própria empresa.
Programa esse que mais tarde veio a tornar Alt na sua primeira vítima.
Atualmente, a sua consciência existe apenas como um fantasma digital na Net."""
Alt.set_info_adicional(info)
# Personagem Predefinido 4
Saburo=Corpo("Saburo Arasaka",10,20)
Saburo.set_cybernetic_implant("?")
info ="""Saburo Arasaka, também conhecido como o Imperador,
passou de piloto do Serviço Aéreo da Marinha Imperial Japonesa a Deus corporativo do século XXI.
Natural de Tóquio, ele transformou a Corporação Arasaka numa das maiores empresas do mundo.
Saburo é orgulhoso, honrado e, como verdadeiro Samurai Shogun, ávido de poder.
Apesar da idade avançada e da debilitação física,
Saburo Arasaka permanece o génio que sempre foi na sua juventude.
Nunca abdicou do controlo sobre a Arasaka,
mesmo quando o seu filho mais velho, Kei, assumiu como Diretor Executivo da Corporação,
mantendo-se como presidente do conselho e o verdadeiro manipulador por trás das principais decisões corporativas.
Depois de décadas a construir a Corporação Arasaka,
Saburo concentrou os seus esforços em bioengenharia e tecnologia de preservação mental.
Chegou até a criar uma cópia digital da sua personalidade, na Sede da Arasaka em Tóquio.
Aos 158 anos, ele ainda reina no topo da Arasaka em 2077,
tendo erguido a empresa como um grande império da sua geração.
É orgulhoso, honrado e implacável."""
Saburo.set_info_adicional(info)
# Personagem Predefinido 5
Smasher=Solo("Adam Smasher",10,20)
Smasher.set_cybernetic_implant("Samson frame")
info ="""Adam Smasher, rival de Morgan blackhand, é um Solo completamente transformado em ciborgue.
Empregado pela Arasaka, em 2077, alcançou o cargo de chefe de segurança e guarda-costas pessoal de Yorinobu Arasaka.
Imponente e praticamente desprovido de humanidade,
Adam passou por uma transformação radical após ser praticamente reduzido a nada por uma explosão de RPG.
Dada a escolha entre ser desligado ou fazer uma conversão total para se tornar um ciborgue,
Adam optou pela segunda opção, mostrando pouco interesse em preservar seu lado humano.
Sem empatia por outros, incluindo seus colegas de trabalho,
Adam é mantido vivo pela Arasaka para eliminar os inimigos da corporação,
podendo apenas ser descrito de uma forma, maldade pura e descontrolada."""
Smasher.set_info_adicional(info)
# Personagem Predefinido 6
Rogue=Fixer("Rogue Amendiares",10,20)
Rogue.set_cybernetic_implant("Visão Cibernética")
info ="""Rogue Amendiares foi bastante famosa durante a década de 2010 em Night City.
Mais tarde tornou-se proprietária do famoso clube noturno Afterlife.
Foi amplamente considerada a melhor fixer da cidade até 2077."""
Rogue.set_info_adicional(info)
# Personagem Predefinido 7
Bartmoss=Netrunner("Rache Bartmoss",10,20)
Bartmoss.set_cybernetic_implant("?")
info ="""Rache Bartmoss foi um lendário Netrunner no início do século XXI.
Ficou famoso como o homem que causou a DataKrash e destruiu a Net.
Ele inventou os programas Demon e Hound.
Juntamente com Spider Murphy, escreveu os livros "Guia para a Net de Rache Bartmoss" e "Explosão de Hardware Cerebral"."""
Bartmoss.set_info_adicional(info)