import java.io.*;
import java.util.*;


public class inputj{
    int n;
    String pathDomain;
    String[] prob;
    String path;
    ArrayList<String> in = new ArrayList<String>();
    public inputj(int n, String prob) {
        this.n = n;
        this.prob = prob.split("_");
        this.path = pathDomain+this.prob[0]+"_"+this.prob[1]+"_"+this.prob[2]+"\"";
        
    }
    void input() throws FileNotFoundException, IOException{
        String filename = Integer.toString(this.n);
        BufferedReader s = new BufferedReader(
                new FileReader(this.path+n+".out")
        );
         while (s.ready()) {
            in.add(
                s.readLine());
        }
        
        
        
    }
    
}
