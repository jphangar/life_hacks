//
//  ViewController.swift
//  Brain Stack
//
//  Created by Jasleen Phangara on 2020-02-08.
//  Copyright © 2020 BrainStack. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    
    @IBOutlet weak var startpage: UIImageView!
    @IBOutlet weak var startbutton: UIButton!
    
    
    @IBOutlet weak var subjects: UIView!
    @IBOutlet weak var backtostart: UIButton!
    
    @IBOutlet weak var math: UIButton!
    @IBOutlet weak var science: UIButton!
    @IBOutlet weak var economics: UIButton!
    @IBOutlet weak var geography: UIButton!
    
    @IBOutlet weak var mathpage: UIView!
    @IBOutlet weak var MBS: UIButton!
    
    
    @IBOutlet weak var Sciencepage: UIView!
    @IBOutlet weak var SBS: UIButton!
    
    
    @IBOutlet weak var economicspage: UIView!
    @IBOutlet weak var EBS: UIButton!
    
    
    @IBOutlet weak var geographypage: UIView!
    @IBOutlet weak var GBS: UIButton!
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func startpressed(_ sender: Any) {
        startpage.isHidden = true
        subjects.isHidden = false
    }
    
    
    @IBAction func backtostartpressed(_ sender: Any) {
        startpage.isHidden = false
        subjects.isHidden = true
    }
    
    @IBAction func mathpressed(_ sender: Any) {
        subjects.isHidden = true
        mathpage.isHidden = false
        
    }
    
    @IBAction func MBSpressed(_ sender: Any) {
        subjects.isHidden = false
        mathpage.isHidden = true
    }
    
    
    @IBAction func sciencepressed(_ sender: Any) {
        subjects.isHidden = true
        Sciencepage.isHidden = false
    }
    
    @IBAction func SBSpressed(_ sender: Any) {
        subjects.isHidden = false
        Sciencepage.isHidden = true
    }
    
    
    @IBAction func economicspressed(_ sender: Any) {
        subjects.isHidden = true
        economicspage.isHidden = false
    }
    
    
    @IBAction func EBSpressed(_ sender: Any) {
        subjects.isHidden = false
        economicspage.isHidden = true
    }
    
    @IBAction func geographypressed(_ sender: Any) {
        subjects.isHidden = true
        geographypage.isHidden = false
    }
    
    
    @IBAction func GBSpressed(_ sender: Any) {
        subjects.isHidden = false
        geographypage.isHidden = true
    }

    
}

