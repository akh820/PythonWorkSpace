# 수업과정에서 필기

네이버 사람들 -> WAS(web application server)를 만든다

operation system 설치돼있음(linux), http protocol - tomcat , 
네이버가 -> 톰캣에 접속을 한다고 표현함
글을 작성하면 -> 영구적으로 저장이 되어야 한다 (database)
누가 저장을 누른다(insert) -> insert에 해당하는 java코드 실행 -> 실행하다가
코드를 읽고 Database로 접속 - > SQL구문을 만들어서 전달해줌[컴퓨터가 3개는 있어야 정상적으로 웹 프로그램이 작동한다, PC,Server,DBMS] -> select 라면 가져온다 -> 
결과적으로 웹 브라우저에 화면이 나와야함 -> html을 리턴해줌(대략적으로, 정확히는아님)
Java, SQL, HTML, JSP(HTML에서 만든 코드를 동적으로 만들어줌), Spring

웹 개발 언어 - 
C, C++, rust, // Java, C#, kotlin //  python, Javascript
실행속도 - 10배정도 빠름 // 객체지향으로써 유지보수 간편 // 작고 적당한 규모에서 사용하기 적당
            컴파일러    // 컴파일러 + 인터프리터        // 인터프리터

Java는 플랫폼에 종속되지 않는다. 이유 JVM이 어떤 플랫폼에서도 실행이 가능
과정 -
a.java -> a.class (컴파일을 통해 생성됨) -> JVM을 통해 실험
대신 단점1. -> 속도가 느려질 수 밖에없다. 컴파일 된것을 JVM을 통해 실행하기 때문에
     단점2. -> OS버전이 올라가면서 API가 생긴다 -> C언어는 바로 쓸 수 있는데, Java는 업데이트 되기 전까지 직접적인 사용이 힘들다.
flutter, react native(java script) = 크로스 플랫폼 !!, 하지만 아직 웹이나 데스크탑 개발은쉽지않다 
dart = flutter에서 사용하는언어 (C와 Java랑 닮아있다.)