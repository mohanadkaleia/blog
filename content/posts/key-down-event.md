Title: Key down event
Date: 2010-12-15 21:43
Author: admin
Category: Code
Slug: key-down-event
Status: published

Hello there..

If you want to execute a code when press a key, this code is what you want

    // Handle the KeyDown event to determine the type of character entered into the control.
    private void textBox1_KeyDown(object sender, System.Windows.Forms.KeyEventArgs e)
    {
       if (e.KeyCode ==Keys.Enter)
         {
            // do some thing
         }
    }

    Enjoy it...
