#include <iostream>
#include <librdkafka/rdkafkacpp.h>

int main(int argc, char *argv[])
{
    std::cout << "hello world" << std::endl;
    RdKafka::Conf *conf = RdKafka::Conf::create(RdKafka::Conf::CONF_GLOBAL);

    std::string errstr;

    if (conf->set("bootstrap.servers", "172.21.100.154:9092", errstr) != RdKafka::Conf::CONF_OK)
    {
        std::cerr << errstr << std::endl;
        return 1;
    }

    RdKafka::Consumer *consumer = RdKafka::Consumer::create(conf, errstr);
    if (!consumer)
    {
        std::cerr << "Failed to create consumer: " << errstr << std::endl;
        return 1;
    }

    std::cout << "% Created consumer " << consumer->name() << std::endl;


    RdKafka::Topic *topic = RdKafka::Topic::create(consumer, "XFace", conf, errstr);
    if (!topic) {
      std::cerr << "Failed to create topic: " << errstr << std::endl;
      exit(1);
    }

    delete conf;

    
    while (true)
    {
        RdKafka::Message *msg = consumer->consume(topic, partition, 1000);
        msg_consume(msg, NULL);
        delete msg;
        consumer->poll(0);
    }

    return 0;
}