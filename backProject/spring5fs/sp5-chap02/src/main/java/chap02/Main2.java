package chap02;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main2 {
    public static void main(String[] arg){
        AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(AppContext.class);
        Greeter g1 = ctx.getBean("greeter", Greeter.class);
        Greeter g2 = ctx.getBean("greeter", Greeter.class);
        Greeter g3 = ctx.getBean("greeter1", Greeter.class);
        System.out.println("(g1==g2) = "+(g1==g2));
        System.out.println("(g1==g3) = "+(g1==g3));
        ctx.close();
    }
}
