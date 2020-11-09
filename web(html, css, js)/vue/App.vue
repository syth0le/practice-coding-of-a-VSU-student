<template>
  <div  class="app">
    <div class="textiknopki">
      <div class="pole">
        <textarea v-model="string" cols="80" rows="50" name="text" placeholder="Введите текст"></textarea>
      </div>
      <div class="knopki">
        <button @click="reverse" class="knopka" >перевернуть</button>
        <button @click="split" class="knopka" >пробел</button>
        <button @click="indexing" class="knopka" >разбиение</button>
        <button @click="counting" class="knopka" >хар-ки текста</button>
      </div>
    </div>
    <p class="textmessage" v-html="result">{{ result }}</p>
  </div>
</template>

<script>
import Vue from 'vue';
import Component from 'vue-class-component';
export default Component({})(
  class App extends Vue {
    result = '';
    string = '';
    reverse() {this.result = this.string.split("").reverse().join("")}
    split() {this.result = this.string.split("").join(" ")}
    indexing() {
      this.len = this.string.length;
      this.finalString = "";
      for (let i = 0; i <= this.len; i++) {
          this.finalString += `${i}: ${this.string[i]}, `;
      }
      this.finalString = this.finalString.split(this.len);
      if (this.finalString[0] === "") {
          this.result = ""
      } else { 
          this.result = this.finalString[0].slice(0,-2) + '.';
      }
    }
    counting() {
      this.textMap = new Map();
      this.len = this.string.length;
      for(let i = 0; i < this.string.length; i++){
          if (this.textMap.has(this.string[i])){
              this.textMap.set(this.string[i], this.textMap.get(this.string[i]) + 1)
          }
          else{this.textMap.set(this.string[i],1)}
      }

      this.finalString = "";
      for (var [letter, value] of this.textMap){
          this.finalString += `${letter}: ${value}, ${(value/this.len).toString().slice(0,4)}%;\n`
      }

      this.temp = this.finalString.slice(0,-2) + '.';
      if (this.temp === ".") {
          this.result = ""
      } else {
          this.result = this.temp
      }
    }
  }
);
</script>

<style>
.pole {
    display: flex;
    width: 250px;
    height: 150px;
    cursor: text;
    white-space: pre-wrap;
    overflow-wrap: break-word;
    font-family: century;
    border-width: 5px;
    border-style: solid;
    border-color: #CD5C5C;
}
.knopka {
    color: white;
    background: #CD5C5C;
    padding: .7em 1.5em;
    outline: none;
    text-align: center;
}
.knopki {
    display: grid;
    justify-content: center;
    grid-template-rows: 60px 60px;
    grid-template-columns: 120px 120px;
    grid-gap: 3vw;
}
.textiknopki {
    display: grid;
    justify-content: center;
    grid-template-rows: 40px 40px;
    grid-template-columns: 80px 80px;
    grid-gap: 300px;
}
.app {
    font-size: 30px;
    color: black;
    text-align: center;
    font-size: 40px;
}
</style>