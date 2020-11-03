import Image from 'next/image'
import styles from '../../styles/Bubble.module.css';
import utilStyles from '../../styles/Utils.module.css';

export default function Bubble({src}: { src: string }) {
  return (
    <div className={`${styles.section}`}>
      <Image
      src={src}
      height="150px"
      width="150px"
      className={`${styles.image} ${utilStyles.borderCircle}`}
      />
    </div>
  )
}