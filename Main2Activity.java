package com.hackfest.kisancare;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Main2Activity extends AppCompatActivity {

    private Button model1Button;
    private Button model2Button;
    private Button model3Button;
    private Button model4Button;
    private Button model5Button;
    private Button extraButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        model1Button = (Button)findViewById(R.id.model1);
        model1Button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openmodel1();
            }
        });
        model2Button = (Button)findViewById(R.id.model2);
        model2Button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openmodel2();
            }
        });
        model3Button = (Button)findViewById(R.id.model3);
        model3Button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openmodel3();
            }
        });

        model4Button = (Button)findViewById(R.id.model4);
        model4Button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openmodel4();
            }
        });

        extraButton = (Button)findViewById(R.id.extra);
        extraButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openextra();
            }
        });

        model5Button = (Button)findViewById(R.id.model5);
        model5Button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openmodel5();
            }
        });

    }
    public void openmodel1(){
        Intent intent = new Intent(this ,model1Activity.class);
        startActivity(intent);
    }

    public void openmodel2(){
        Intent intent = new Intent(this ,model2Activity.class);
        startActivity(intent);
    }

    public void openmodel3(){
        Intent intent = new Intent(this ,model3Activity.class);
        startActivity(intent);
    }

    public void openmodel4(){
        Intent intent = new Intent(this ,model4Activity.class);
        startActivity(intent);
    }

    public void openextra(){
        Intent intent = new Intent(this ,extraActivity.class);
        startActivity(intent);
    }
    public void openmodel5(){
        Intent intent = new Intent(this ,model5Activity.class);
        startActivity(intent);
    }

}
