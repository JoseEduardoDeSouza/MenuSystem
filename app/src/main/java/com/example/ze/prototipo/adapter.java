package com.example.ze.prototipo;

import android.app.Activity;
import android.content.ClipData;
import android.content.Context;
import android.support.annotation.NonNull;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.BaseAdapter;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ze on 03/12/16.
 */

public class adapter extends BaseAdapter {

    private List<ItemLanche> listaItens;
    private LayoutInflater inflater;

    public adapter(Context contexto, List<ItemLanche> listaItens) {
        this.listaItens = listaItens;
        this.inflater = LayoutInflater.from(contexto);
    }

    @Override
    public int getCount() {
        return listaItens.size();
    }

    @Override
    public Object getItem(int posicao) {
        return listaItens.get(posicao);
    }

    @Override
    public long getItemId(int posicao) {
        return posicao;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        ItemSuporte itemSuporte;

        if (view == null) {
            view = inflater.inflate(R.layout.alanche, null);

        }
        final ItemLanche item = listaItens.get(i);

        itemSuporte = new ItemSuporte();
        itemSuporte.lancheView = ((TextView) view.findViewById(R.id.textoLanche));
        itemSuporte.checkBox = (CheckBox) view.findViewById(R.id.checar);
        itemSuporte.checkBox.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                Log.d("Checar","Entrou");
                item.setChecar(b);


            }
        });

        itemSuporte.lancheView.setText(item.getLanche());



        return view;
    }


    private class ItemSuporte {
        public TextView lancheView;
        public CheckBox checkBox;

    }
}