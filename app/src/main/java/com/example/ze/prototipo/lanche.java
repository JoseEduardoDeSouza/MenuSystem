package com.example.ze.prototipo;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ze on 03/12/16.
 */

public class lanche extends AppCompatActivity {

    String lanche;
    ListView listaView;
    public static adapter adaptador;
    public static List<ItemLanche> itemLanche;
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.lanche);
        listaView = (ListView) findViewById(R.id.listaLanche);
        itemLanche = new ArrayList<ItemLanche>();

        adaptador = new adapter(this, itemLanche);
        listaView.setAdapter(adaptador);
    }
    public void add(View view) {
        EditText novo = (EditText) findViewById(R.id.addLanche);
        lanche = novo.getText().toString();

        atualizaLista(lanche);

    }
    public void carregar(){

    }

    public void atualizaLista(final String lanche) {

        ItemLanche novoItem = new ItemLanche(lanche);
        itemLanche.add(novoItem);
        listaView.setAdapter(adaptador);
        listaView.setSelection(adaptador.getCount() - 1);


        }


}

