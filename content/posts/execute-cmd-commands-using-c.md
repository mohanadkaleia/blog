Title: Execute cmd commands using C#
Date: 2011-11-24 12:56
Author: admin
Category: Code
Slug: execute-cmd-commands-using-c
Status: published

    Hello again , 
    If you want to execute cmd commands from c# you can use this method : 

    private void ExecuteCommand(string Command)
    {
        ProcessStartInfo ProcessInfo;
        Process Process;

        ProcessInfo = new ProcessStartInfo("cmd.exe", "/C " + Command);
        ProcessInfo.CreateNoWindow = false;
        ProcessInfo.UseShellExecute = false;
        Process = Process.Start(ProcessInfo);
        Process.WaitForExit();

        Process.Close();
    }

    If you like to execute multi commands in the same process you can just seperate each one with "&"

    like this : 


    ExecuteCommand("cd & myApp.exe");

    where "cd" is the first command and "myApp.exe" is the second one.

    Enjoy it..
