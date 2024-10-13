#include <stdio.h>
#include <stdbool.h>

typedef enum { frame_arrival } event_type;

typedef struct {
    char info[100]; 
} packet;

typedef struct {
    packet info;
} frame;

void from_network_layer(packet* p) {

    snprintf(p->info, sizeof(p->info), "Data");
}

void to_physical_layer(frame* f) {
    
    printf("Sending frame: %s\n", f->info.info);
}

void from_physical_layer(packet* p) {
    
    snprintf(p->info, sizeof(p->info), "Data");
}

void to_network_layer(frame* f) {
    
    printf("Received frame: %s\n", f->info.info);
}

void sender1(int numPackets) {
    frame s;        
    packet buffer;   

    for (int i = 0; i < numPackets; i++) {
        from_network_layer(&buffer);
        s.info = buffer;          
        to_physical_layer(&s);   
    }
}

void receiver1(int numPackets) {
    frame s;        
    packet buffer;   

    for (int i = 0; i < numPackets; i++) {
        from_physical_layer(&s.info); 
        buffer = s.info;              
        to_network_layer(&s);    
    }
}

int main() {
    int numPackets;

    printf("Enter the number of packets: ");
    scanf("%d", &numPackets);

    sender1(numPackets); // Start the sender thread
    receiver1(numPackets); // Start the receiver thread

    return 0;
}
