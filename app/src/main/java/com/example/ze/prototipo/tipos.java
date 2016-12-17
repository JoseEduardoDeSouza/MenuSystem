package com.example.ze.prototipo;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.Toast;

/**
 * Created by ze on 29/11/16.
 */

public class tipos extends AppCompatActivity{
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.tipos);
    }

    public void bebida(View view){

        Intent intent1 = new Intent(tipos.this, bebida.class);
        startActivityForResult(intent1,0);
    }
    public void lanche(View view){

        Intent intent2 = new Intent(tipos.this, lanche.class);
        startActivity(intent2);
    }
    public void porcao(View view){

        Intent intent3 = new Intent(tipos.this, porcao.class);
        startActivity(intent3);
    }

}
