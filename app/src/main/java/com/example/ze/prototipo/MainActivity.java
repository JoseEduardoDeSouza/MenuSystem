package com.example.ze.prototipo;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private String[] items;
    Spinner s;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        this.items = new String[] {
                "1", "2", "3", "4", "5"
        };
        s = (Spinner) findViewById(R.id.spinner);
        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,
                android.R.layout.simple_spinner_item, items);
        s.setAdapter(adapter);
        fun(s);

    }
    public void fun(final AdapterView s) {
        s.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String Mesa = s.getSelectedItem().toString();
                Toast.makeText(MainActivity.this, Mesa, Toast.LENGTH_SHORT).show();

            }
            public void onNothingSelected(AdapterView<?> adapterView) {
                return;
            }
        });


    }
    public void butao(View v) {
        Intent intent = new Intent(MainActivity.this, tipos.class);
        startActivity(intent);

    }


}
