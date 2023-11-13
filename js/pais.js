"use strict"
class Pais {
    constructor(nombre_pais, nombre_capital, population) {
        this.nombre = nombre_pais;
        this.capital = nombre_capital;
        this.population = population;

        inicializa_resto_atributos();
    }

    inicializa_resto_atributos() {
        this.tipo_gobierno="autocracia";
        this.coordenadas=["47.5361","-18.9136","0"];
        this.religion="cristianismo";
    }

    get_nombre() {
        return this.nombre;
    }

    get_capital() {
        return this.capital;
    }

    get_population() {
        return this.population;
    }

    get_tipo_gobierno() {
        return this.tipo_gobierno;
    }

    get_coordenadas() {
        // formato: "latitud,longitud,altitud"
        return `${this.coordenadas[0]},${this.coordenadas[1]},${this.coordenadas[2]}`;
    }

    get_religion() {
        return this.religion;
    }

    get_informacion_secundaria() {
        // Lista con población, tipo de gobierno y religion mayoritaria
        let lista_HTML5 = `
        <ul>
            <li>Población: ${this.population}</li>
            <li>Forma de gobierno: ${this.tipo_gobierno}</li>
            <li>Religión mayoritaria: ${this.religion}</li>
        </ul>`;
        return lista_HTML5;
    }

    write_coordenadas() {
        document.write(`Latitud: ${this.coordenadas[0]},
                        Longitud: ${this.coordenadas[1]}
                        Altitud: ${this.coordenadas[2]}`)
    }
}

// objeto madagascar, capital Antananarivo, población 28,92 millones
var madagascar = new Pais("Madagascar", "Antananarivo", "28.920.000");