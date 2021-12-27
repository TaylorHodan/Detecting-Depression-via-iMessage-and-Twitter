//
//  ViewController.swift
//  ResearchProject
//
//  Created by Taylor Hodan on 2020-12-28.
//

import UIKit
import SafariServices
import SwiftUI

class ViewController: UIViewController {
    
    @IBOutlet weak var textField: UITextField!
    @IBOutlet weak var textView: UITextView!
    @IBOutlet weak var scaleImage: UIImageView!
    @IBOutlet weak var scaleGreen: UIImageView!
    @IBOutlet weak var scaleYellow: UIImageView!
    @IBOutlet weak var scaleOrange: UIImageView!
    @IBOutlet weak var scaleOrange2: UIImageView!
    @IBOutlet weak var scaleRed: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        scaleImage.isHidden=false
        scaleGreen.isHidden=true
        scaleYellow.isHidden=true
        scaleOrange.isHidden=true
        scaleOrange2.isHidden=true
        scaleRed.isHidden=true
    }
    
    @IBAction func setText(_ sender: UIButton){
        let tText = textField.text
        textField.text = tText
        
        let display = ""
        let text: String? = tText
        let num = Int(text!) ?? 0
        if (num <= 18) {
            let display = "No to Minimal Depression"
            textView.text = display
            scaleGreen.isHidden=false
            scaleYellow.isHidden=true
            scaleOrange.isHidden=true
            scaleOrange2.isHidden=true
            scaleRed.isHidden=true
        }
        else if (num <= 37) {
            let display = "Mild Depression"
            textView.text = display
            scaleYellow.isHidden=false
            scaleGreen.isHidden=true
            scaleOrange.isHidden=true
            scaleOrange2.isHidden=true
            scaleRed.isHidden=true
        }
        else if (num <= 56) {
            let display = "Moderate Depression"
            textView.text = display
            scaleOrange.isHidden=false
            scaleGreen.isHidden=true
            scaleYellow.isHidden=true
            scaleOrange2.isHidden=true
            scaleRed.isHidden=true
        }
        else if (num <= 75) {
            let display = "Moderately Severe Depression"
            textView.text = display
            scaleOrange2.isHidden=false
            scaleGreen.isHidden=true
            scaleYellow.isHidden=true
            scaleOrange.isHidden=true
            scaleRed.isHidden=true
        }
        else {
            let display = "Severe Depression"
            textView.text = display
            scaleRed.isHidden=false
            scaleGreen.isHidden=true
            scaleYellow.isHidden=true
            scaleOrange.isHidden=true
            scaleOrange2.isHidden=true
        }
        
        textView.text += display
        scaleImage.isHidden=true
    }

}
