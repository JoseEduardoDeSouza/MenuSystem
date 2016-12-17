package com.example.ze.prototipo;

/**
 * Created by ze on 03/12/16.
 */

public class ItemLanche {
    private String lanche;
    private Boolean setChecar;

    public Boolean getChecar() {
        return checar;
    }

    public void setChecar(Boolean checar) {
        this.setChecar= checar;
    }

    private Boolean checar
            ;

    public ItemLanche(String lanche) {
        this.lanche = lanche;
    }

    public ItemLanche() {
        this.lanche = "";

    }
    public String getLanche() {
        return lanche;
    }

    public void setTexto(String lanche) {
        this.lanche = lanche;
    }
}



