package com.example.user.androidapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class LogInActivity extends AppCompatActivity {
    EditText username;
    EditText password;
    Button register;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_log_in);
        username = (EditText)findViewById(R.id.Username);
        password =  (EditText)findViewByID(R.id.Password);
        register = (Button)findViewById(R.id.register);

    }
    protected void registerClick(View view)
    {
        startActivity(new Intent(MainActivity.this,registerAct2.class));
    }

}
