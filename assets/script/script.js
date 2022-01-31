var racas = [
    {"raca": "humano", "cidade":["Vermênia", "Estátira", "Divinópolis", "Tandra", "Gashbad"], "atributos":[{"player_atk": Math.floor(Math.random() * 5+1), "player_sab": Math.floor(Math.random() * 5+1), "player_vel": Math.floor(Math.random() * 5+1), "player_per": Math.floor(Math.random() * 5+1), "player_const": Math.floor(Math.random() * 5+1)}]},
    {"raca": "ciclope", "cidade":["Glúkdra", "Mashshag", "Agar'roch", "Ugarg", "Warkatopia"], "atributos":[{"player_atk": 0, "player_sab": 0, "player_vel": 0, "player_per": 0, "player_const": 0, }]},
    {"raca": "elfo", "cidade":["Alqualondë", "Avallonè", "Brithombar", "Eldamar", "Ithilien"], "atributos":[{"player_atk": 0, "player_sab": 0, "player_vel": 0, "player_per": 0, "player_const": 0, }]}
]
var numRand = Math.floor(Math.random() * 3)
var ouro = 30
var xp = 20
var pontoAtributos = 3


// alert("Bem vindo ao RPG EXTREMAMENTE experimental do Jhony")


var radios = document.getElementsByName('raca');
function saveName(){
    nome = (document.getElementById("nome").value)
    nome = nome.charAt(0).toUpperCase() + nome.slice(1)
    if (nome == "Bezos"){
        ouro = 999999
    }
    for (var indice = 0; indice < radios.length; indice++) {
        if (radios[indice].checked) {
          var index = radios[indice].value
          var racaEscolha = racas[index].raca
          var reinoNasc = racas[index].cidade[numRand]
          var player_atk = racas[index].atributos[0].player_atk
          var player_sab = racas[index].atributos[0].player_sab
          var player_vel = racas[index].atributos[0].player_vel
          var player_per = racas[index].atributos[0].player_per
          var player_const = racas[index].atributos[0].player_const
          var atributos = "Ataque: <span>"+player_atk+
          "</span><br>Sabedoria: <span>"+player_sab+
          "</span><br>Velocidade: <span>"+player_vel+
          "</span><br>Percepção: <span>"+player_per+
          "</span><br>Constituição: <span>"+player_const+"</span>";}
        }
    if (nome != "" && reinoNasc != undefined) {
        texto = ("<div>Seu nome é <span>"+nome+"</span>, um <span>"+racaEscolha+"</span> nascido e criado na cidade de <span>"+reinoNasc+
        "</span>. Você tem <span>"+ouro+"</span> de ouro e <span>"+xp+"</span> de XP.<br>Seus atributos são:<br>"+atributos+"<br>Você tem <span>"+pontoAtributos+
        "</span> pontos pra distribuir entre os atributos, deseja distribuir agora?</div><br><button id="+"simbutton"+" onclick="+"adicionaAtributos()"+">SIM</button><button id="+"naobutton"+" onclick="+"prosseguir()"+">NÃO</button>")
        function initialText(){document.getElementById("conteudo").innerHTML = texto}
        initialText()
    }else {document.getElementById("msg").innerHTML = "Hey! Por favor preencha o campo que falta!"
            function shakeThat(){document.getElementById("msg").style.animation = "shake 0.2s"}
            shakeThat()
           }
}