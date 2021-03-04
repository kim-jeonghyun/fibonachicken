# fibonachicken

Cowork flow

## PM

1. 자신의 github 계정에서 repository를 생성하여 clone한다.
2. clone한 자신의 repo에서 git flow init 하여 대상 파일을 생성한 뒤 develop 브랜치에 push 한다.
3. 팀원에게 fork 할 것을 알린 후, repository에서 projects 생성과 milestone 설정을 완료한다.
4. 팀원과 함께 프로젝트 진행방향과 역할을 나누며, 토의를 진행한다.

## Dev team

1. fork 요청을 받은 이후, 팀장의 repo에 방문하여 fork를 진행한다.
2. 토의 진행 후 팀장의 repo에 방문하여, 자신이 할 일에 대해 issue를 생성한다.
3. fork하여 나의 소유가 된 repo를 clone한다.
4. git flow init 하여 develop 브랜치를 생성하고, feature start 하여 기능 개발에 착수한다.
5. 기능 개발 완료 후 feature를 finish하고, 자신의 develop에 push한다.
6. fork 한 나의 repo에 재방문 하여 compare & pull request 를 생성한다. (dev -> dev 주의!!)
6-1. 이때 내가 만든 issue number와 resolved를 함께적어 issue와 pull request를 link한다.

## PM

5. 팀원의 pull request 도착 후, 해당 페이지에 방문하여 code review를 진행한다.
6. 추가 수정이 필요할 경우 커뮤니케이션을 활용하여 재요청한다.
(이때 Dev team은 추가 요청에 응하여 develop 브랜치에서 작업하여 바로 add, commit, push를 진행)

7. 최종 완료시 merge 하여 해당 pull request를 완료한다.

## Dev Team
7. 작업 중 다른 팀원이 pull request를 merge 하였을 경우, 나의 develop을 팀장의 develop과 최신화를 실시한다.

(팀장 repo 추가 필수: git remote add pmorigin 팀장주소)

`$ git pull pmorigin develop`
