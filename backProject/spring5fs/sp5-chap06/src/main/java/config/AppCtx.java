package config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

// import spring.Client;
import spring.Client2;

@Configuration
public class AppCtx{
    
    // @Bean
    // public Client client(){
    //     Client client = new Client();
    //     client.setHost("host");
    //     return client;
    // }

    // 주의할 점
    // @Bean
    // public Client client(){
    //     Client client = new Client();
    //     client.setHost("host");
    //     client.afterPropertiesSet();
    //     return client;
    // }

    // @Bean(initMethod = "connect", destroyMethod = "close")
    // public Client2 client2(){
    //     Client2 client = new Client2();
    //     client.setHost("host");
    //     return client;
    // }

    @Bean(destroyMethod = "close")
    public Client2 client2(){
        Client2 client = new Client2();
        client.setHost("host");
        client.connect();
        return client;
    }
}