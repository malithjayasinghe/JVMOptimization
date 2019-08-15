import ballerina/io;
import ballerina/time;
import ballerina/log;

public function main() returns error?{
    string dstFileName ="response_time.txt";
    float sumArea = 0.0;
    int startTime1 = time:nanoTime();
    int numRuns = 10000;


    foreach var i in 1..<numRuns{
        float x0 = 0;
        float xn = 100;
        int n = 1000;
        sumArea = sumArea + trapezoidal(x0, xn, n);
     }

     int endTime = time:nanoTime();
     anydata runTime = ((endTime - startTime1)/(1000000.00));
     //io:WritableByteChannel writableFileResult = check io:openWritableFile(dstFileName,true);
     io:WritableByteChannel writableFileResult = check io:openWritableFile(dstFileName);
     io:WritableCharacterChannel destinationChannel = new(writableFileResult, "UTF-8");
     var  writeCharResult1 = check destinationChannel.write(runTime.toString(), 0);
     var cr = destinationChannel.close();
      if (cr is error) {
             log:printError("Error occured while closing the channel: ", err = cr);
     }
}

function trapezoidal(float a, float b, int n) returns (float)
{
    //Grid spacing
    float h = (b-a)/n;
    // Computing sum of first and last terms
    // in above formula

    float s = y(a)+y(b);
    //Adding middle terms in above formula

    foreach var i in 1..< n {
        s += 2* y (a+ i* h);
     }
    // h/2 indicates (b-a)/2n. Multiplying h/2
    // with s.
    return (h/2)*s;
}

function y(float x) returns (float)
{
    // Declaring the function f(x) = 1/(1+x*x)
    return 1/(1+x*x);
}

