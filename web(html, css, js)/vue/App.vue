<template>
    <div id="app">
        <textarea id="dataoutput" rows="10" cols="50" v-model="text"></textarea>
        <div id="buttons">
            <button class="submit-button btn1" @click="reverseData">Reverse</button>
            <button class="submit-button btn2" @click="splitData">Split</button>
            <button class="submit-button btn3" @click="indexingData">Index</button>
            <button class="submit-button btn4" @click="countingData">Count</button>
            <button class="submit-button btn5" @click="deleteData">Delete</button>
        </div>
        <p class="textmessage" v-html="message">{message}</p>
    </div>
</template>

<script>
    // Vue entry:
    new Vue({
        el: '#app',
        data: {
            text:'',
            message:'',
        },
        methods: {
            reverseData: function(reverseData) {
                this.message = this.text.split("").reverse().join("");
            },
            splitData: function() {
                this.message = this.text.split("").join(" ").split("   ").join(" ");
            },
            indexingData: function() {
                this.len = this.text.length;
                this.finalString = "";
                for (let i = 0; i <= this.len; i++) {
                    this.finalString += `${i}: ${this.text[i]}, `;
                }
                this.finalString = this.finalString.split(this.len);
                if (this.finalString[0] === "") {
                    this.message = ""
                } else {
                    this.message = this.finalString[0].slice(0,-2) + '.';
                }
            },
            countingData: function() {
                this.textMap = new Map();
                this.len = this.text.length;
                try {
                    for(let i = 0; i < this.text.length; i++){
                        if (this.textMap.has(this.text[i])){
                            this.textMap.set(this.text[i], this.textMap.get(this.text[i]) + 1)
                        }
                        else{this.textMap.set(this.text[i],1)}
                    }
                } catch {}
                this.finalString = "";
                for (var [letter, value] of this.textMap){
                    this.finalString += `${letter}: ${value}, ${(value/this.len).toString().slice(0,4)}%;\n`
                }
                this.temp = this.finalString.slice(0,-2) + '.';
                if (this.temp === ".") {
                    this.message = ""
                } else {
                    this.message = this.temp
                }
            },
            deleteData: function() {
                this.text = "";
                this.message = "";
                alert("Вы удалили сообщение!")
            }
        }
    });
</script>

<style>
    #dataoutput {
        position: relative;
        margin-left: auto;
        margin-right: auto;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    #buttons{
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
    }
    .submit-button{
        margin: 10px;
    }
    .textmessage{
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
    }
</style>