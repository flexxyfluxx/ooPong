import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

/**
 *
 * Main Menu fuer OOPong.
 *
 * @version 1.0 vom 12.05.2022
 * @flyxx 
 */

public class MainMenu extends JFrame {
  // Anfang Attribute
  // start attributes
  private JButton jbtn_play = new JButton();
  private JLabel jLabel1 = new JLabel("PONK!", SwingConstants.CENTER);
  public JTextField jtf_wndw_height = new JTextField();
  public JTextField jtf_wndw_width = new JTextField();
  public JTextField jtf_ball_speed = new JTextField();
  public JToggleButton jtb_obstacles = new JToggleButton();
  private JLabel jLabel2 = new JLabel("Spielfensterhoehe");
  private JLabel jLabel3 = new JLabel("Spielfensterbreite");
  private JLabel jLabel4 = new JLabel("Hindernisse");
  private JLabel jLabel5 = new JLabel("Ballgeschwindigkeit");
  private JSeparator jSeparator1 = new JSeparator();
  public JButton jbtn_kbind_left_up = new JButton();
  public JButton jbtn_kbind_right_up = new JButton();
  public JButton jbtn_kbind_left_dn = new JButton();
  public JButton jbtn_kbind_right_dn = new JButton();
  public JButton jbtn_save_settings = new JButton();
  private JSeparator jSeparator2 = new JSeparator();
  private JLabel jLabel6 = new JLabel("Keybinds", SwingConstants.CENTER);
  private JLabel jLabel7 = new JLabel("Links Hoch", SwingConstants.CENTER);
  private JLabel jLabel8 = new JLabel("Rechts Hoch", SwingConstants.CENTER);
  private JLabel jLabel9 = new JLabel("Links Runter", SwingConstants.CENTER);
  private JLabel jLabel10 = new JLabel("Rechts Runter", SwingConstants.CENTER);
  private JLabel jLabel11 = new JLabel("Anklicken, um Aenderungen vorzunehmen!", SwingConstants.CENTER);
  // end attributes
  // Ende Attribute
  
  public MainMenu() { 
    // Frame-Initialisierung
    super();
    setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
    int frameWidth = 351; 
    int frameHeight = 552;
    setSize(frameWidth, frameHeight);
    Dimension d = Toolkit.getDefaultToolkit().getScreenSize();
    int x = (d.width - getSize().width) / 2;
    int y = (d.height - getSize().height) / 2;
    setLocation(x, y);
    setTitle("Ponk! - Main Menu");
    setResizable(false);
    Container cp = getContentPane();
    cp.setLayout(null);
    // Anfang Komponenten
    
    jbtn_play.setBounds(73, 74, 195, 57);
    jbtn_play.setText("Spielen!");
    jbtn_play.setFont(new Font("Arial", Font.PLAIN, 24));
    jbtn_play.setMargin(new Insets(2, 2, 2, 2));
    jbtn_play.addActionListener(new ActionListener() { 
      public void actionPerformed(ActionEvent evt) { 
        //jbtn_play_ActionPerformed(evt);
      }
    });
    cp.add(jbtn_play);
    jLabel1.setBounds(7, 3, 326, 60);
    jLabel1.setFont(new Font("Arial", Font.BOLD, 48));
    cp.add(jLabel1);
    jtf_wndw_height.setBounds(255, 160, 75, 20);

    jtf_wndw_width.setBounds(255, 190, 75, 20);

    jtf_ball_speed.setBounds(255, 250, 75, 20);

    jtb_obstacles.setBounds(255, 217, 75, 25);

    jLabel2.setBounds(10, 160, 230, 20);

    jLabel3.setBounds(10, 190, 230, 20);

    jLabel4.setBounds(10, 220, 230, 20);

    jLabel5.setBounds(10, 250, 230, 20);

    jtf_wndw_height.setText("");
    cp.add(jtf_wndw_height);
    jtf_wndw_width.setText("");
    cp.add(jtf_wndw_width);
    jtf_ball_speed.setText("");
    cp.add(jtf_ball_speed);
    jtb_obstacles.setText("Ein/Aus");
    jtb_obstacles.setMargin(new Insets(2, 2, 2, 2));
    jtb_obstacles.addActionListener(new ActionListener() { 
      public void actionPerformed(ActionEvent evt) { 
        //jtb_obstacles_ActionPerformed(evt);
      }
    });
    cp.add(jtb_obstacles);
    cp.add(jLabel2);
    cp.add(jLabel3);
    cp.add(jLabel4);
    cp.add(jLabel5);
    jSeparator1.setBounds(0, 143, 335, 10);
    cp.add(jSeparator1);
    jbtn_kbind_left_up.setBounds(40, 380, 75, 25);
    jbtn_kbind_left_up.setText("left_up");
    jbtn_kbind_left_up.setMargin(new Insets(2, 2, 2, 2));
    jbtn_kbind_left_up.addActionListener(new ActionListener() { 
      public void actionPerformed(ActionEvent evt) { 
        //jbtn_kbind_left_up_ActionPerformed(evt);
      }
    });
    cp.add(jbtn_kbind_left_up);
    jbtn_kbind_right_up.setBounds(218, 380, 75, 25);
    jbtn_kbind_right_up.setText("right_up");
    jbtn_kbind_right_up.setMargin(new Insets(2, 2, 2, 2));
    jbtn_kbind_right_up.addActionListener(new ActionListener() { 
      public void actionPerformed(ActionEvent evt) { 
        //jbtn_kbind_right_up_ActionPerformed(evt);
      }
    });
    cp.add(jbtn_kbind_right_up);
    jbtn_kbind_left_dn.setBounds(40, 450, 75, 25);
    jbtn_kbind_right_dn.setBounds(218, 450, 75, 25);
    jbtn_kbind_left_dn.setText("left_dn");
    jbtn_kbind_left_dn.setMargin(new Insets(2, 2, 2, 2));
    jbtn_kbind_left_dn.addActionListener(new ActionListener() { 
      public void actionPerformed(ActionEvent evt) { 
        //jbtn_kbind_left_dn_ActionPerformed(evt);
      }
    });
    cp.add(jbtn_kbind_left_dn);
    jbtn_kbind_right_dn.setText("right_dn");
    jbtn_kbind_right_dn.setMargin(new Insets(2, 2, 2, 2));
    jbtn_kbind_right_dn.addActionListener(new ActionListener() { 
      public void actionPerformed(ActionEvent evt) { 
        //jbtn_kbind_right_dn_ActionPerformed(evt);
      }
    });
    cp.add(jbtn_kbind_right_dn);
    jbtn_save_settings.setBounds(71, 280, 187, 25);
    jbtn_save_settings.setText("Einstellungen speichern");
    jbtn_save_settings.setMargin(new Insets(2, 2, 2, 2));
    jbtn_save_settings.addActionListener(new ActionListener() { 
      public void actionPerformed(ActionEvent evt) { 
        //jbtn_save_settings_ActionPerformed(evt);
      }
    });
    cp.add(jbtn_save_settings);
    jSeparator2.setBounds(0, 310, 337, 9);
    cp.add(jSeparator2);
    jLabel6.setBounds(4, 325, 326, 20);
    cp.add(jLabel6);
    jLabel7.setBounds(20, 355, 110, 20);
    cp.add(jLabel7);
    jLabel8.setBounds(198, 355, 110, 20);
    cp.add(jLabel8);
    jLabel9.setBounds(20, 425, 110, 20);
    cp.add(jLabel9);
    jLabel10.setBounds(198, 425, 110, 20);
    cp.add(jLabel10);
    jLabel11.setBounds(4, 485, 326, 20);
    cp.add(jLabel11);
    // Ende Komponenten
    
    //setVisible(true);
  } // end of public MainMenu
  
  // start methods
  
  // Anfang Methoden
  
  public static void main(String[] args) {
    new MainMenu();
  } // end of main
  
  public void jbtn_play_ActionPerformed(ActionEvent evt) {
    // TODO hier Quelltext einfuegen
    
  } // end of jbtn_play_ActionPerformed

  public void jtb_obstacles_ActionPerformed(ActionEvent evt) {
    // TODO hier Quelltext einfuegen
    
  } // end of jtb_obstacles_ActionPerformed

  public void jbtn_kbind_left_up_ActionPerformed(ActionEvent evt) {
    // TODO hier Quelltext einfuegen
    
  } // end of jbtn_kbind_left_up_ActionPerformed

  public void jbtn_kbind_right_up_ActionPerformed(ActionEvent evt) {
    // TODO hier Quelltext einfuegen
    
  } // end of jbtn_kbind_right_up_ActionPerformed

  public void jbtn_kbind_left_dn_ActionPerformed(ActionEvent evt) {
    // TODO hier Quelltext einfuegen
    
  } // end of jbtn_kbind_left_dn_ActionPerformed

  public void jbtn_kbind_right_dn_ActionPerformed(ActionEvent evt) {
    // TODO hier Quelltext einfuegen
    
  } // end of jbtn_kbind_right_dn_ActionPerformed
  public void jbtn_save_settings_ActionPerformed(ActionEvent evt) {
    // TODO add your code here
    
  } // end of jbtn_save_settings_ActionPerformed

  // end methods

  // Ende Methoden
} // end of class MainMenu
