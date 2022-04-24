## 1 and 2

query{
  quiz
  allQuizzes{
    id
    title
  }
  allQuestions(id:1){
    title
    #quiz
  }
  allAnswers(id:1){
    answerText
  }
}


## 2

query GetQuestion($id: Int = 1){
  quiz
  allQuizzes{
    id
    title
  }
  allQuestions(id:$id){
    title
    #quiz
  }
  allAnswers(id:$id){
    answerText
  }
}

## 3
## update
mutation firstmutation{
  newCategory(id:3, name: "poglitest"){
    category{
      name
    }
  }
}

## 4
## add
mutation firstmutation{
  newCategory(name: "poglitest"){
    category{
      name
    }
  }
}

## 5
## delete
mutation firstmutation{
  newCategory(id:3){
    category{
      name
    }
  }
}

