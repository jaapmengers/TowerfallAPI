package com.example

import rx.lang.scala.Observable
import scala.concurrent.duration._
import scala.language.postfixOps

object Hello {
  sealed trait Prediction
  case object Korjan extends Prediction
  case object Jaap extends Prediction

  sealed trait GameInfo
  case object StartGame extends GameInfo
  case object EndGame extends GameInfo

  def main(args: Array[String]): Unit = {
    val predictionsForControllers = List(0, 1).map { x =>
      Observable.interval(200 millis).map { _ =>
        if(x == 0) Korjan else Jaap
      }
    }

    val predictions = Observable.combineLatest(predictionsForControllers)(identity)

    val gameInfoObservable: Observable[GameInfo] = Observable.interval(2 seconds).flatMap {
      case 0 => Observable.just(StartGame)
      case _ => Observable.from(List(EndGame, StartGame))
    }

    val starts = gameInfoObservable.collect {
      case StartGame => StartGame
    }

    val closings = gameInfoObservable.collect {
      case EndGame => EndGame
    }

    val snor = predictions.slidingBuffer(starts)(_ => closings)

    snor.subscribe(x => println(s"Results: ${x.length}"))

//    val gameCount = gameInfoObservable.collect {
//      case StartGame => StartGame
//    }.scan(0)((x, _) => x + 1)


//    val combined = predictions.combineLatest(gameCount)
//
//    val groups = combined.group (x => x._2)
//
//    groups.flatMap { x =>
//      x._2.toList
//    }.subscribe(println(_))





//
//
//    val starts = gameInfoObservable.collect {
//      case StartGame => StartGame
//    }
//
//    val stops = gameInfoObservable.collect {
//      case EndGame => EndGame
//    }
//
//    starts.subscribe { _ =>
//      println("Start")
//
//      stops.take(1).subscribe(_ => println("Stop"))
//
////      predictionsForControllers.foreach { (pc, index) =>
////        pc.takeUntil(stops).toList.subscribe { predictions =>
////          println(s"Predictions for ")
////        }
////      }
//    }

    while(true){
      Thread.sleep(2000)
    }
  }
}
