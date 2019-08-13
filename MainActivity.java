package com.hackfest.kisancare;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener{

    private Button button;
    Spinner s1,s2;
    String district[]=null;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        s1 = (Spinner)findViewById(R.id.spinner1);
        s2 = (Spinner)findViewById(R.id.spinner2);


        s1.setOnItemSelectedListener(this);
        button = (Button) findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                openActivity2();
            }
        });
    }
    @Override
    public void onItemSelected(AdapterView<?> arg0, View arg1, int arg2, long arg3) {
        if(arg2==0){
            district=new String[]{"Bhagalpur","Darbhanga","Katihar","Jamaui","Gaya","Nawada","Samastipur","Purni","Patna","Gopalganj",""};
        }
        if(arg2==1){
            district=new String[]{"Dhanbad","Ranchi","Dumka","Deoghar"};
        }
        if(arg2==2){
            district=new String[]{"Amritsar","Bhatinda","Firozpur","Ludhiana"};
        }
        if(arg2==3){
            district=new String[]{"Panchkula","Hansi","Panipat","Hisar"};
        }
        ArrayAdapter<String> adt =new ArrayAdapter<String>(this ,android.R.layout.simple_list_item_1,district);
        s2.setAdapter(adt);
    }

    @Override
    public void onNothingSelected(AdapterView<?> arg0) {

    }

    public void openActivity2(){
        Intent intent = new Intent(this, Main2Activity.class);
        startActivity(intent);
    }
}
