## 포켓몬 피카츄 레벨업 로직

포켓몬세상, 포켓몬을 진화시키기 위해서는 진화사탕 12개가 들어간다.\
오박사에게 진화사탕 12개와 피카츄를 데려가면,\
오박사는 라이츄로 진화를 시켜줌과 동시에,\
보너스 경험치(XP) 500XP와 보너스 사탕 1개를 준다.

피카츄의 주인 지우가 만약 피카츄 13마리와 1개의 진화사탕이 있어도
진화시킬 방법은 있다.

피카츄 한마리를 오박사에게 주면 진화사탕 1개로 교체를 해준다.\
(단, 피카츄를 돌려받을 수는 없다.)\
위 방법으로 지우가 13마리 중 11마리를 사탕으로 교체하면 2마리의 피카츄와 12개의 진화사탕을 갖게된다.\
따라서, 지우는 피카츄 한마리를 진화 시킬 수 있다.

* 오박사는 사탕을 아무리 가져다 주어도 피카츄로 바꿔주지 않는다.

> 문제\
지우가 데리고 다니는 피카츄의 수와, 사탕수를 대입했을때, 가장 많은 보너스 경험치를 리턴하는 함수를 짜시오.\
\
`SOULUTION(pikachu, candy);`\
\
조건\
솔루션 함수에는 첫번째 인자로 피카츄 마리 수(0 이상의 정수), 사탕 수 (0 이상의 정수)

```js
const SOULUTION = (pika, candy) => {
    //1 pika === 1 candy
    let getNewXp = 0;
    let getNewCandy = 0;
    let remainCandy = candy;
    let remainPika = pika;
    const OPT = {
        lvup_candy: 12,
        baseXP: 500,
        newCandy: 1
    };
    const LV_UP_FN = (p, c) => {
        const CAN_LV_UP_PIKA = Math.floor(c / OPT.lvup_candy);
        getNewXp = getNewXp + CAN_LV_UP_PIKA * OPT.baseXP;
        getNewCandy = CAN_LV_UP_PIKA * OPT.newCandy;
        remainCandy = (c % OPT.lvup_candy) + getNewCandy;
        remainPika = p - CAN_LV_UP_PIKA;
        // console.log('=== p', p);
        // console.log('=== c', c);
        // console.log(getNewXp, getNewCandy);
        // console.log('\tremainCandy', remainCandy);
        // console.log('\tremainPika', remainPika);
        const NEED_CANDY = OPT.lvup_candy - remainCandy; //11
        // console.log('/NEED_CANDY', NEED_CANDY);
        if (remainPika >= NEED_CANDY + 1) {
            remainPika = remainPika - NEED_CANDY;
            remainCandy = remainCandy + NEED_CANDY;
            return true;
        } else {
            return false;
        }
        // console.log('NEED_CANDY', NEED_CANDY);
    };
    while (remainPika >= 1) {
        if (!LV_UP_FN(remainPika, remainCandy)) break;
    }
    console.log('final', getNewXp);
    return getNewXp;
    //1차 끝

    //1, 12 == 1, 1 ,11
    //
    // return xp;
};

SOULUTION(1, 12); // 결과 : 500
SOULUTION(13, 144); // 결과 :  6500
SOULUTION(10, 63); // 결과 :  3000
SOULUTION(4, 9); // 결과 : 2500
SOULUTION(630, 1); // 결과 : 26000
SOULUTION(0, 12); // 결과 : 0
SOULUTION(550, 0); // 결과 : 22500
```