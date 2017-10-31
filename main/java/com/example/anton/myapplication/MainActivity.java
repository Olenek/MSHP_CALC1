package com.example.anton.myapplication;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends Activity implements View.OnClickListener {


    View view;
    Button btnRed;
    Button btnGrn;
    Button btnYlw;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        view = this.getWindow().getDecorView();
        view.setBackgroundResource(R.color.colorPrimary);
        btnRed = (Button) findViewById(R.id.btnR);
        btnGrn = (Button) findViewById(R.id.btnG);
        btnYlw = (Button) findViewById(R.id.btnY);

        btnRed.setOnClickListener(this);
        btnGrn.setOnClickListener(this);
        btnYlw.setOnClickListener(this);

    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btnY:
                view.setBackgroundResource(R.color.colorYellow);
                break;
            case R.id.btnG:
                view.setBackgroundResource(R.color.colorGreen);
                break;
            case R.id.btnR:
                view.setBackgroundResource(R.color.colorRed);
                break;
            default:
                break;
        }
    }
}