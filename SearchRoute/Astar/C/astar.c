#include <stdio.h>

#define ARRAY_NUM(a) (sizeof(a)/sizeof(a[0]))
#define NODE_MAX 1000

struct NODE {
    int i;
    int j;
    int cost;
    struct NODE *parent;
};
typedef struct NODE NODE;

struct LIST {
    NODE *node[NODE_MAX];
    int index;
};
typedef struct LIST LIST;

NODE *create_node(int i,int j,int cost) {
    // とりあえずmallocとか使わずに固定
    static NODE n[NODE_MAX];
    static int index = 0;
    n[index].i = i;
    n[index].j = j;
    n[index].cost = cost;
    return &n[index++];
}

int g (NODE *s,NODE *n) {
    return n->cost;
}

int h (NODE *e,NODE *n) {
    return 0;
}

void search_node(LIST *open,LIST *close,NODE *s,NODE *e,NODE *n,NODE *m) {
    int in_open = -1;
    int in_close = -1;
    int i;
    int fdmcost = g(s,n) + h(e,m) + 1;
    int fsmcost = g(s,m) + h(e,m);
    
    // mがopenリストに含まれているか
    for(i=0;i<open->index;i++) {
        if ( open->node[i] != NULL && m->i == open->node[i]->i && m->j == open->node[i]->j ) {
            in_open = i;
            break;
        }
    }
    
    // mがcloseリストに含まれているか
    for(i=0;i<close->index;i++) {
        if ( close->node[i] != NULL && m->i == close->node[i]->i && m->j == close->node[i]->j ) {
            in_close = i;
            break;
        }
    }
    
    // m が Openリストにも Closeリストにも含まれていない場合
    if ( in_open == -1 && in_close == -1 ) {
        m->parent = n;
        open->node[open->index++] = m;
    }
    
    if ( in_open > -1 ) {
        if ( fdmcost < fsmcost ) {
            m->parent = n;
        }
    }
    
    if ( in_close > -1 ) {
        if ( fdmcost < fsmcost ) {
            m->parent = n;
            open->node[open->index++] = m;
            close->node[in_close] = NULL;
        }
    }
}


int main(void) {
    FILE *fp;
    char map[13][25]; // マップの大きさは考慮しない
    char buf[28];
    int i=0;
    int j=0;
    int loop=0;
    NODE s={0,0,0};
    NODE e={0,0,0};
    LIST open;
    LIST close;
    open.index=0;
    close.index=0;
    
    if ( fopen_s(&fp,"map.txt","r") != 0 ) {
        return 1;
    }
    while( fgets(buf,sizeof(buf),fp) != NULL ){
        for(j=0;j<26;j++){
            map[i][j] = buf[j];
        }
        i++;
    }
    fclose(fp);
    
    for(i=0;i<ARRAY_NUM(map);i++) {
        for(j=0;j<26;j++) {
            if(map[i][j] == 'S'){
                s.i=i;
                s.j=j;
                open.node[open.index++] = &s;
            }
            if(map[i][j] == 'G'){
                e.i=i;
                e.j=j;
            }
        }
    }
    
    while (1) {
        NODE *n = NULL;
        for(i=0;i<open.index;i++) {
            if ( open.node[i] != NULL ) {
                int cost = g(&s,open.node[i]);
                if ( n == NULL || n->cost > cost ) {
                    // ノードの中で一番最小のコストを得る
                    n = open.node[i];
                    open.node[i] = NULL;
                }
            }
        }
        
        // openからリストがなくなったので終了する
        if ( n == NULL ) {
            printf("no goal...\n");
            break;
        }
        
        // もしGなら終了する
        if ( map[n->i][n->j] == 'G' ) {
            printf("ok goal!!!\n");
            
            n = n->parent;
            while(n->parent!=NULL) {
                map[n->i][n->j] = '$';
                n = n->parent;
            }
            
            break;
        }
        
        close.node[close.index++] = n;
        
        // 上のノードを検索
        if ( n->i >= 1 && map[n->i-1][n->j] == ' ' || map[n->i-1][n->j] == 'G' ) {
            search_node(&open,&close,&s,&e,n,create_node(n->i-1,n->j,n->cost+1));
        }
        
        // 下のノードを検索
        if ( n->i <= 11 && map[n->i+1][n->j] == ' ' || map[n->i+1][n->j] == 'G' ) {
            search_node(&open,&close,&s,&e,n,create_node(n->i+1,n->j,n->cost+1));
        }
        
        // 右のノードを検索
        if ( n->j <= 24 && map[n->i][n->j+1] == ' ' || map[n->i][n->j+1] == 'G' ) {
            search_node(&open,&close,&s,&e,n,create_node(n->i,n->j+1,n->cost+1));
        }
        
        // 左のノードを検索
        if ( n->j >= 1 && map[n->i][n->j-1] == ' ' || map[n->i][n->j-1] == 'G' ) {
            search_node(&open,&close,&s,&e,n,create_node(n->i,n->j-1,n->cost+1));
        }
        
        if ( loop++ > 1000 ) { printf("loop error...\n"); break; }
    }
    
    for(i=0;i<ARRAY_NUM(map);i++) {
        for(j=0;j<26;j++) {
            printf("%c",map[i][j]);
        }
        printf("\n");
    }

    return 0;
}
