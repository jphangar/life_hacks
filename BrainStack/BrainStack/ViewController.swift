//
//  ViewController.swift
//  BrainStack
//
//  Created by Jasleen Phangara on 2020-02-08.
//

import UIKit

class ViewController: UIViewController {
    
    
    @IBOutlet weak var startpage: UIImageView!
    @IBOutlet weak var startbutton: UIButton!
    @IBOutlet weak var subjects: UIView!
    
    @IBOutlet weak var subjects_back: UIImageView!
    @IBOutlet weak var math: UIButton!
    @IBOutlet weak var Science: UIButton!
    @IBOutlet weak var economics: UIButton!
    @IBOutlet weak var geography: UIButton!
    @IBOutlet weak var back_to_start: UIButton!
    
    @IBOutlet weak var mathpage: UIView!
    @IBOutlet weak var mathback: UIImageView!
    @IBOutlet weak var algebra: UIButton!
    @IBOutlet weak var MBS: UIButton!
    @IBOutlet weak var Caculus: UIButton!
    @IBOutlet weak var Function: UIButton!
    
    @IBOutlet weak var Sciencepage: UIView!
    @IBOutlet weak var SBS: UIButton!
    
    @IBOutlet weak var Econpage: UIView!
    @IBOutlet weak var EBS: UIButton!
    
    @IBOutlet weak var Geogpage: UIView!
    @IBOutlet weak var GBS: UIButton!
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    
    @IBAction func startbuttonpressed(_ sender: Any) {
        subjects.isHidden = false
        startpage.isHidden = true
        startbutton.isHidden = true
    }
    
    
    @IBAction func backStart(_ sender: Any) {
        subjects.isHidden = true
        startpage.isHidden = false
        startbutton.isHidden = false
    }
    
    
    @IBAction func mathpressed(_ sender: Any) {
        mathpage.isHidden = false
    }
    
    
    @IBAction func MBSpressed(_ sender: Any) {
        mathpage.isHidden = true
    }
    
    @IBAction func sciencepressed(_ sender: Any) {
        Sciencepage.isHidden = false
    }
    
    @IBAction func SBSpressed(_ sender: Any) {
        Sciencepage.isHidden = true
    }
    
    
    @IBAction func econpressed(_ sender: Any) {
        Econpage.isHidden = false
    }
    
    
    @IBAction func EBSpressed(_ sender: Any) {
        Econpage.isHidden = true
    }
    
    
    @IBAction func geographypressed(_ sender: Any) {
        Geogpage.isHidden = false
    }
    
    @IBAction func GBSpressed(_ sender: Any) {
        Geogpage.isHidden = true
    }
    
    
    
    
    
    
    
}

